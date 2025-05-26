# Fájl neve: generate_plan.py
# Elérési út: /scripts/

import os
import openai
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

# Egyszerű bemenet: active_plan.txt
with open("scripts/active_plan.txt", "r", encoding="utf-8") as f:
    plan_request = f.read()

# Prompt sablon: fix struktúra
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
    model="gpt-4",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.2
)

output = response["choices"][0]["message"]["content"]

os.makedirs("scripts/output", exist_ok=True)
with open("scripts/output/screen_plan.md", "w", encoding="utf-8") as f:
    f.write(output)

print("Terv generálva: screen_plan.md")
