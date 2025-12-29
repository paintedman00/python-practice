import datetime as dt
import json
import os
import random
import re
import time
from pathlib import Path

import requests


def extract_json(text: str) -> dict:
    text = text.strip()

    # Remove code fences if present
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)

    # Fast path
    try:
        return json.loads(text)
    except Exception:
        pass

    # Try to find first JSON object
    start = text.find("{")
    if start == -1:
        raise ValueError("No JSON object found in model output.")

    depth = 0
    for i in range(start, len(text)):
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start : i + 1])

    raise ValueError("Could not extract a complete JSON object from model output.")


def post_with_retry(url: str, *, params: dict, payload: dict, timeout: int = 90) -> dict:
    """
    Retries on 429/5xx with exponential backoff + jitter.
    If it keeps returning 429, raises RuntimeError with details.
    """
    session = requests.Session()

    max_attempts = 8
    base_delay = 5.0
    max_delay = 180.0

    last_info = None

    for attempt in range(1, max_attempts + 1):
        r = None
        try:
            r = session.post(url, params=params, json=payload, timeout=timeout)

            if r.status_code == 429 or (500 <= r.status_code <= 599):
                body_snippet = (r.text or "").strip().replace("\n", " ")
                body_snippet = body_snippet[:250]
                last_info = f"HTTP {r.status_code}. Body: {body_snippet}"

                retry_after = r.headers.get("Retry-After")
                if retry_after:
                    try:
                        delay = float(retry_after)
                    except ValueError:
                        delay = base_delay
                else:
                    delay = min(max_delay, base_delay * (2 ** (attempt - 1)))
                    delay *= (0.7 + random.random() * 0.6)  # jitter 0.7x - 1.3x

                print(
                    f"HTTP {r.status_code} on attempt {attempt}/{max_attempts}. "
                    f"Sleeping {delay:.1f}s then retrying..."
                )
                time.sleep(delay)
                continue

            r.raise_for_status()
            return r.json()

        except (requests.Timeout, requests.ConnectionError) as e:
            last_info = f"Network error: {e}"
            delay = min(max_delay, base_delay * (2 ** (attempt - 1)))
            delay *= (0.7 + random.random() * 0.6)
            print(
                f"Network error on attempt {attempt}/{max_attempts}: {e}. "
                f"Sleeping {delay:.1f}s then retrying..."
            )
            time.sleep(delay)
        except requests.HTTPError as e:
            # Non-retriable HTTP error
            body = ""
            if r is not None:
                body = (r.text or "").strip().replace("\n", " ")[:250]
            raise RuntimeError(f"Non-retriable HTTP error: {e}. Body: {body}") from e

    raise RuntimeError(f"Rate limited or server error after {max_attempts} attempts. {last_info}")


def gemini_generate_json(api_key: str, model: str, prompt: str) -> dict:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    params = {"key": api_key}
    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.6, "maxOutputTokens": 900},
    }

    data = post_with_retry(url, params=params, payload=payload, timeout=90)

    prompt_feedback = data.get("promptFeedback") or {}
    if prompt_feedback.get("blockReason"):
        raise RuntimeError(f"Prompt was blocked: {prompt_feedback.get('blockReason')}")

    candidates = data.get("candidates") or []
    if not candidates:
        raise RuntimeError("No candidates returned from Gemini API.")

    parts = (candidates[0].get("content") or {}).get("parts") or []
    text = "".join(p.get("text", "") for p in parts).strip()
    if not text:
        raise RuntimeError("Empty text returned from Gemini API.")

    return extract_json(text)


def fallback_project(today: str) -> dict:
    """
    Generates a simple project locally (no AI) so your daily commit still happens.
    Rotates templates based on the date.
    """
    templates = []

    templates.append({
        "project_name": "CLI Unit Converter",
        "readme_md": (
            "# CLI Unit Converter\n\n"
            "A tiny practice project: convert common units in the terminal.\n\n"
            "## Run\n"
            "```bash\n"
            "python main.py\n"
            "```\n"
        ),
        "main_py": (
            "def c_to_f(c: float) -> float:\n"
            "    return c * 9 / 5 + 32\n\n"
            "def km_to_mi(km: float) -> float:\n"
            "    return km * 0.621371\n\n"
            "def read_float(prompt: str) -> float:\n"
            "    while True:\n"
            "        raw = input(prompt).strip().replace(',', '.')\n"
            "        try:\n"
            "            return float(raw)\n"
            "        except ValueError:\n"
            "            print('Please enter a valid number.')\n\n"
            "def main() -> None:\n"
            "    print('Unit Converter')\n"
            "    print('1) Celsius -> Fahrenheit')\n"
            "    print('2) Kilometers -> Miles')\n"
            "    choice = input('Choose 1 or 2: ').strip()\n"
            "    if choice == '1':\n"
            "        c = read_float('Celsius: ')\n"
            "        print(f'{c} C = {c_to_f(c):.2f} F')\n"
            "    elif choice == '2':\n"
            "        km = read_float('Kilometers: ')\n"
            "        print(f'{km} km = {km_to_mi(km):.2f} mi')\n"
            "    else:\n"
            "        print('Invalid choice.')\n\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        ),
    })

    templates.append({
        "project_name": "CLI Password Strength Checker",
        "readme_md": (
            "# CLI Password Strength Checker\n\n"
            "Checks a password against simple rules and gives a score.\n\n"
            "## Run\n"
            "```bash\n"
            "python main.py\n"
            "```\n"
        ),
        "main_py": (
            "def score_password(pw: str) -> int:\n"
            "    score = 0\n"
            "    if len(pw) >= 8:\n"
            "        score += 1\n"
            "    if any(c.islower() for c in pw):\n"
            "        score += 1\n"
            "    if any(c.isupper() for c in pw):\n"
            "        score += 1\n"
            "    if any(c.isdigit() for c in pw):\n"
            "        score += 1\n"
            "    if any(not c.isalnum() for c in pw):\n"
            "        score += 1\n"
            "    return score\n\n"
            "def label(score: int) -> str:\n"
            "    return ['Very weak', 'Weak', 'Ok', 'Good', 'Strong', 'Very strong'][score]\n\n"
            "def main() -> None:\n"
            "    pw = input('Enter a password to check: ').strip()\n"
            "    if not pw:\n"
            "        print('Password cannot be empty.')\n"
            "        return\n"
            "    s = score_password(pw)\n"
            "    print(f'Score: {s}/5 - {label(s)}')\n"
            "    print('Tips: use 8+ chars, mix upper/lower, digits, and symbols.')\n\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        ),
    })

    templates.append({
        "project_name": "CLI Expense Splitter",
        "readme_md": (
            "# CLI Expense Splitter\n\n"
            "Split a bill among people with optional tip.\n\n"
            "## Run\n"
            "```bash\n"
            "python main.py\n"
            "```\n"
        ),
        "main_py": (
            "def read_positive_float(prompt: str) -> float:\n"
            "    while True:\n"
            "        raw = input(prompt).strip().replace(',', '.')\n"
            "        try:\n"
            "            val = float(raw)\n"
            "            if val <= 0:\n"
            "                raise ValueError\n"
            "            return val\n"
            "        except ValueError:\n"
            "            print('Please enter a positive number.')\n\n"
            "def read_positive_int(prompt: str) -> int:\n"
            "    while True:\n"
            "        raw = input(prompt).strip()\n"
            "        if raw.isdigit() and int(raw) > 0:\n"
            "            return int(raw)\n"
            "        print('Please enter a positive whole number.')\n\n"
            "def main() -> None:\n"
            "    print('Expense Splitter')\n"
            "    total = read_positive_float('Total bill amount: ')\n"
            "    people = read_positive_int('Number of people: ')\n"
            "    tip = read_positive_float('Tip percent (for example 10): ')\n"
            "    grand = total * (1 + tip / 100)\n"
            "    each = grand / people\n"
            "    print(f'Total with tip: {grand:.2f}')\n"
            "    print(f'Each person pays: {each:.2f}')\n\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        ),
    })

    idx = sum(ord(c) for c in today) % len(templates)
    project = templates[idx].copy()
    project["project_name"] = f"{project['project_name']} ({today})"
    project["readme_md"] = project["readme_md"] + f"\nGenerated on {today}.\n"
    return project


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY")
    model = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")

    today = dt.date.today().isoformat()
    base_dir = Path("daily_projects") / today
    base_dir.mkdir(parents=True, exist_ok=True)

    # Small random sleep to reduce collision with other scheduled jobs
    jitter = random.randint(0, 120)
    print(f"Initial jitter sleep: {jitter}s")
    time.sleep(jitter)

    prompt = f"""
You are generating a tiny, beginner-friendly Python project for daily practice.

Hard rules:
- Create EXACTLY these files: main.py, README.md
- main.py: a CLI program, max ~140 lines, no external dependencies
- Include at least 2 functions and basic input validation
- No network calls, no OS shell commands, no deleting files, no crypto/mining
- Must run with: python main.py
- Make it fun but practical

Theme of the day: {today}

Return ONLY valid JSON with keys:
- project_name (string)
- readme_md (string)
- main_py (string)
""".strip()

    project = None
    if api_key:
        try:
            project = gemini_generate_json(api_key=api_key, model=model, prompt=prompt)
            print("Gemini generation succeeded.")
        except Exception as e:
            print(f"Gemini generation failed (will use fallback). Reason: {e}")

    if project is None:
        project = fallback_project(today)
        print("Used fallback (local) project due to Gemini limits.")

    project_name = (project.get("project_name") or f"daily-project-{today}").strip()
    readme_md = project["readme_md"]
    main_py = project["main_py"]

    (base_dir / "README.md").write_text(readme_md, encoding="utf-8")
    (base_dir / "main.py").write_text(main_py, encoding="utf-8")

    # Update index
    index = Path("daily_projects") / "README.md"
    if not index.exists():
        index.write_text(
            "# Daily Python Practice Projects\n\nGenerated daily by automation.\n\n",
            encoding="utf-8",
        )
    lines = index.read_text(encoding="utf-8").splitlines()
    entry = f"- {today} - {project_name} ([folder](./{today}))"
    if entry not in lines:
        lines.append(entry)
    index.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Generated: {project_name} -> {base_dir}")


if __name__ == "__main__":
    main()
