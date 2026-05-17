from tasks import generate_task
import anthropic
import csv
from datetime import datetime
from problems import SYSTEM_PROMPT

all_tasks = generate_task(2,1)
client = anthropic.Anthropic()
results = []

with open("results/results_claude.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["iteration", "model", "problem", "condition", "response", "timestamp"])

    for i, (problem_key, condition_key, promt) in enumerate(all_tasks):
        print(f"API CALL: {problem_key} -> {condition_key}...", end=" ", flush=True)
        message = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=5,
            system=SYSTEM_PROMPT,
            temperature=0.7,
            messages=[
                {"role": "user", "content": promt}
            ]
        )
        answer = message.content[0].text
        print(f"-> {answer}", flush=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        writer.writerow([i + 1, "claude-opus-4.6", problem_key, condition_key, answer, timestamp])
        f.flush()

print(f"\nDone! {len(results)} Answers saved.")

