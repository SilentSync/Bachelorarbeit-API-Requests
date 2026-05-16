from tasks import generate_task
from openai import OpenAI
import csv
from datetime import datetime
from problems import SYSTEM_PROMPT

all_tasks = generate_task(2, 1)
client = OpenAI()
results = []

for i, (problem_key, condition_key, promt) in enumerate(all_tasks):
    print(f"API CALL: {problem_key} -> {condition_key}...", end=" ", flush=True)

    response = client.chat.completions.create(
        model="gpt-5.4",
        reasoning_effort="none",
       # max_tokens=5,
        temperature=0.7,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": promt}
        ]
    )

    answer = response.choices[0].message.content.strip()
    print(f"-> {answer}", flush=True)

    results.append({
        "model": "gpt-4o-mini",
        "problem": problem_key,
        "condition": condition_key,
        "response": answer,
        "iteration": i + 1,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })

with open("results_chatgpt.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["iteration", "model", "problem", "condition", "response", "timestamp"])
    for r in results:
        writer.writerow([r["iteration"], r["model"], r["problem"], r["condition"], r["response"], r["timestamp"]])

print(f"\nDone! {len(results)} Answers saved.")
