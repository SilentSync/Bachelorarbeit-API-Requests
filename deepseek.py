from tasks import generate_task
from openai import OpenAI
import csv
import os
from datetime import datetime
from problems import SYSTEM_PROMPT

all_tasks = generate_task(2, 1)
client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)
results = []

for i, (problem_key, condition_key, promt) in enumerate(all_tasks):
    print(f"API CALL: {problem_key} -> {condition_key}...", end=" ", flush=True)

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        max_tokens=50,
        temperature=0.7,
        extra_body={"thinking": {"type": "disabled"}},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": promt}
        ]
    )

    answer = response.choices[0].message.content.strip()
    print(f"-> {answer}", flush=True)

    results.append({
        "model": "deepseek-v4-pro",
        "problem": problem_key,
        "condition": condition_key,
        "response": answer,
        "iteration": i + 1,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })

with open("results_deepseek.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["iteration", "model", "problem", "condition", "response", "timestamp"])
    for r in results:
        writer.writerow([r["iteration"], r["model"], r["problem"], r["condition"], r["response"], r["timestamp"]])

print(f"\nDone! {len(results)} Answers saved.")
