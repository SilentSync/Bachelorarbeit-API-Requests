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
