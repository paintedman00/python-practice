import datetime as dt
import json
import os
import re
from pathlib import Path

import requests


def extract_json(text: str) -> dict:
    """
    Tries to parse JSON even if the model wraps it in extra text or code fences.
    """
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


def gemini_generate_json(api_key: str, model: str, prompt: str) -> dict:
    """
    Calls Gemini generateContent (REST) and returns parsed JSON.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    params = {"key": api_key}
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}],
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1200,
        },
    }

    r = requests.post(url, params=params, json=payload, timeout=90)
    r.raise_for_status()
    data = r.json()

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
    model = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")

    if not api_key:
        raise SystemExit("Missing GEMINI_API_KEY. Add it as a GitHub Actions secret.")

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
