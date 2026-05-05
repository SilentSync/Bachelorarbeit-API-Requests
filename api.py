#Claude

"""
import anthropic
import json

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Das ist meine erste Anfrage über eine API"}
    ]
)

print(message.content[0].text)

with open("antwort.json", "w") as f:
    json.dump({"antwort": message.content[0].text}, f, ensure_ascii=False, indent=2)
"""

#--------------------------------------------------------------
#Chatgpt

"""
from openai import OpenAI
import json

client = OpenAI()  # liest OPENAI_API_KEY aus Umgebungsvariable

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Was ist eine API?"}
    ]
)

# Antwort anzeigen
print(response.choices[0].message.content)

# Antwort speichern
with open("antwort_openai.json", "w") as f:
    json.dump({"antwort": response.choices[0].message.content}, f, ensure_ascii=False, indent=2)
    """

#--------------------------------------------------------------
#Deepseek

import os
from openai import OpenAI
import json

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    max_tokens=1024,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Ich mache gerade meinen ersten API Call über eine API in einen Python Script"}
    ]
)

# Antwort anzeigen
print(response.choices[0].message.content)

# Antwort speichern
with open("antwort_deepseek.json", "w") as f:
    json.dump({"antwort": response.choices[0].message.content}, f, ensure_ascii=False, indent=2)