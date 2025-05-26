import openai
import os

# GPT API kulcs beállítása (GitHub Secrets vagy CI env változóként ajánlott)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Prompt sablon beolvasása (templates/module_prompt.txt)
def load_prompt_template():
    with open("templates/module_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()

# Issue-ból nyert adat + blueprint egyesítése prompttá
def build_prompt(issue_description, blueprint):
    template = load_prompt_template()
    return template.replace("{{ISSUE_DESCRIPTION}}", issue_description).replace("{{PROJECT_BLUEPRINT}}", blueprint)

# GPT hívás (GPT-4o javasolt)
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a senior Flutter developer AI agent."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

# Fő generálási függvény
def generate_module(issue_path, blueprint_path):
    with open(issue_path, "r", encoding="utf-8") as f:
        issue_content = f.read()
    with open(blueprint_path, "r", encoding="utf-8") as f:
        blueprint_content = f.read()

    prompt = build_prompt(issue_content, blueprint_content)
    generated = generate_response(prompt)

    output_path = "generated/module_output.md"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(generated)
    print("✅ Modul generálva: ", output_path)

# Ha önállóan futtatjuk (pl. local script vagy CI-ben)
if __name__ == "__main__":
    generate_module(".github/ISSUE_TEMPLATE/current_issue.md", "docs/blueprints/project_blueprint.md")
