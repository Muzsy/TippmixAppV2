# generate_all.py
# /scripts/

import os
import re
import shutil
import subprocess
import openai
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT_TEMPLATE_PATH = "templates/agent_prompt_template.txt"
ISSUE_PATH = "scripts/active_issue.txt"
PLAN_OUTPUT_PATH = "scripts/output/screen_plan.md"
GENERATED_TXT_PATH = "scripts/output/{screen}_generated.txt"
RULES_PATH = "scripts/rules/coding_rules.json"

def extract(tag, text):
    match = re.search(fr"{tag}:(.*)", text)
    return match.group(1).strip() if match else ""

def load_issue_data():
    with open(ISSUE_PATH, "r", encoding="utf-8") as f:
        data = f.read()
    return {
        "screen_name": extract("screen_name", data),
        "description": extract("description", data),
        "widget_files": extract("widget_files", data),
        "service_files": extract("service_files", data),
        "model_files": extract("model_files", data),
        "functions": extract("functions", data),
        "commit_message": extract("commit_message", data)
    }

def load_rules():
    with open(RULES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_screen_plan(plan_request):
    prompt = f"""
Kérem, csak egy tervet generálj az alábbi képernyőhöz:

{plan_request}

Struktúrát kérek Markdown formában:
- Mit fog tartalmazni a képernyő
- Milyen adatokat kezel
- Milyen fájlok jönnek létre (előzetes becslés)
- Edge case-ek
- Lokalizációs kulcsok prefixe
- Tesztelhetőség fő szempontjai

Csak tervezői választ kérek, ne generálj kódot.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    with open(PLAN_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(response["choices"][0]["message"]["content"])

def generate_code_from_template(data):
    with open(PROMPT_TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    prompt = template
    for key, value in data.items():
        if key == "commit_message":
            continue
        prompt = prompt.replace(f"{{{{{key}}}}}", value)

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    generated_txt_path = GENERATED_TXT_PATH.format(screen=data["screen_name"])
    if os.path.exists(generated_txt_path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        shutil.copy(generated_txt_path, generated_txt_path.replace(".txt", f"_backup_{timestamp}.txt"))

    with open(generated_txt_path, "w", encoding="utf-8") as f:
        f.write(response["choices"][0]["message"]["content"])

    return generated_txt_path

def split_generated_file(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_file = None
    buffer = []
    for line in lines:
        match = re.match(r"/// Fájlnév: (.*)", line)
        if match:
            if current_file and buffer:
                write_file(current_file, buffer)
                buffer = []
            current_file = match.group(1).strip()
        elif current_file:
            buffer.append(line)

    if current_file and buffer:
        write_file(current_file, buffer)

def write_file(path, lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)

def check_localization_in_dart(rules):
    missing = []
    text_regex = re.compile(rules["text_regex"])
    for root, _, files in os.walk("lib"):
        if any(excl in root for excl in rules.get("excluded_dirs", [])):
            continue
        for file in files:
            if file.endswith(".dart"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if rules.get("localization_required", True):
                        for match in text_regex.finditer(content):
                            if rules["localization_check"] not in content:
                                missing.append((path, match.group(0)))
    return missing

def run_flutter_tests():
    if not os.path.exists("test") or not any(f.endswith(".dart") for f in os.listdir("test")):
        print("⚠️  Nincs teszt futtatva: nincs tesztfájl a 'test/' mappában.")
        return True, ""

    result = subprocess.run(["flutter", "test"], capture_output=True, text=True)
    return result.returncode == 0, result.stdout

def git_commit_and_push(commit_message):
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    data = load_issue_data()
    rules = load_rules()
    generate_screen_plan(data["description"])
    txt_path = generate_code_from_template(data)
    split_generated_file(txt_path)

    localization_issues = check_localization_in_dart(rules)
    if localization_issues:
        print("❌ Lokalizációs hiba a következő sorokban:")
        for file, line in localization_issues:
            print(f"{file}: {line}")
        exit(1)

    passed, test_output = run_flutter_tests()
    if not passed:
        print("❌ Tesztek elbuktak:\n", test_output)
        exit(1)
    else:
        print("✅ Minden teszt sikeres.")

    git_commit_and_push(data["commit_message"])
    print("✅ Git commit + push sikeres.")
