import os
import json
import datetime as dt
from pathlib import Path

import requests


API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")

if not API_KEY:
    raise SystemExit("Missing OPENAI_API_KEY. Add it as a GitHub Actions secret.")

today = dt.date.today().isoformat()
base_dir = Path("daily_projects") / today
base_dir.mkdir(parents=True, exist_ok=True)

prompt = f"""
Generate a tiny, beginner-friendly Python project for daily practice.

Hard rules:
- Create EXACTLY these files: main.py, README.md
- main.py: a CLI program, max ~140 lines, no external dependencies
- At least 2 functions + simple input validation
- No network calls, no shell commands, no deleting files, no crypto/mining
- Must run with: python main.py

Theme of the day: {today}

Return ONLY valid JSON with keys:
- project_name (string)
- readme_md (string)
- main_py (string)
"""

url = "https://api.openai.com/v1/responses"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}
payload = {
    "model": MODEL,
    "input": prompt,
}

r = requests.post(url, headers=headers, json=payload, timeout=90)
r.raise_for_status()
data = r.json()

# Extract text from Responses API output
text = ""
for item in data.get("output", []):
    for c in item.get("content", []):
        if c.get("type") in ("output_text", "text"):
            text += c.get("text", "")

text = text.strip()
project = json.loads(text)

project_name = (project.get("project_name") or f"daily-project-{today}").strip()
readme_md = project["readme_md"]
main_py = project["main_py"]

(base_dir / "README.md").write_text(readme_md, encoding="utf-8")
(base_dir / "main.py").write_text(main_py, encoding="utf-8")

# Update an index README
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

print(f"Generated {project_name} -> {base_dir}")
