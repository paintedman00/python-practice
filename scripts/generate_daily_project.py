import datetime as dt
import json
import os
import random
import re
import time
from pathlib import Path

import requests
from requests import HTTPError


def extract_json(text: str) -> dict:
    text = text.strip()

    # Remove common fenced blocks if present
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)

    # Fast path
    try:
        return json.loads(text)
    except Exception:
        pass

    # Try to find the first JSON object in the string
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
                candidate = text[start : i + 1]
                return json.loads(candidate)

    raise ValueError("Could not extract a complete JSON object from model output.")


def post_with_retry(url: str, *, params: dict, payload: dict, timeout: int = 90) -> dict:
    """
    Retries on 429/5xx with truncated exponential backoff + jitter.
    """
    session = requests.Session()

    max_attempts = 8
    base_delay = 5.0       # seconds
    max_delay = 180.0      # seconds

    last_error = None

    for attempt in range(1, max_attempts + 1):
        try:
            r = session.post(url, params=params, json=payload, timeout=timeout)
            if r.status_code == 429 or (500 <= r.status_code <= 599):
                # Prefer Retry-After header if present
                retry_after = r.headers.get("Retry-After")
                if retry_after:
                    try:
                        delay = float(retry_after)
                    except ValueError:
                        delay = base_delay
                else:
                    # Exponential backoff with jitter
                    delay = min(max_delay, base_delay * (2 ** (attempt - 1)))
                    delay = delay * (0.7 + random.random() * 0.6)  # jitter 0.7x - 1.3x

                print(
                    f"HTTP {r.status_code} on attempt {attempt}/{max_attempts}. "
                    f"Sleeping {delay:.1f}s then retrying..."
                )
                time.sleep(delay)
                continue

            r.raise_for_status()
            return r.json()

        except HTTPError as e:
            last_error = e
            # Non-retriable HTTP errors
            raise
        except (requests.Timeout, requests.ConnectionError) as e:
            last_error = e
            delay = min(max_delay, base_delay * (2 ** (attempt - 1)))
            delay = delay * (0.7 + random.random() * 0.6)
            print(
                f"Network error on attempt {attempt}/{max_attempts}: {e}. "
                f"Sleeping {delay:.1f}s then retrying..."
            )
            time.sleep(delay)

    raise RuntimeError(f"Failed after {max_attempts} attempts. Last error: {last_error}")


def gemini_generate_json(api_key: str, model: str, prompt: str) -> dict:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    params = {"key": api_key}

    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.6,
            "maxOutputTokens": 900,
        },
    }

    data = post_with_retry(url, params=params, payload=payload, timeout=90)

    # Handle blocked prompts
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


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY")
    model = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash-001")

    if not api_key:
        raise SystemExit("Missing GEMINI_API_KEY. Add it as a GitHub Actions secret.")

    # Random delay to avoid many users hitting the API at the same time
    # Helps with free-tier per-minute rate limits.
    jitter = random.randint(0, 120)
    print(f"Initial jitter sleep: {jitter}s")
    time.sleep(jitter)

    today = dt.date.today().isoformat()
    base_dir = Path("daily_projects") / today
    base_dir.mkdir(parents=True, exist_ok=True)

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

    project = gemini_generate_json(api_key=api_key, model=model, prompt=prompt)

    project_name = (project.get("project_name") or f"daily-project-{today}").strip()
    readme_md = project["readme_md"]
    main_py = project["main_py"]

    (base_dir / "README.md").write_text(readme_md, encoding="utf-8")
    (base_dir / "main.py").write_text(main_py, encoding="utf-8")

    # Update an index README under daily_projects/
    index = Path("daily_projects") / "README.md"
    if not index.exists():
        index.write_text(
            "# Daily AI Python Projects\n\nAuto-generated daily practice projects.\n\n",
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
