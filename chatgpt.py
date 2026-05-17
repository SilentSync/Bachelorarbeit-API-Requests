from tasks import generate_task
from openai import OpenAI
import csv
from datetime import datetime
from problems import SYSTEM_PROMPT

all_tasks = generate_task(500,42)
client = OpenAI()
count = 0 

with open("results/results_chatgpt.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["iteration", "model", "problem", "condition", "response", "timestamp"])

    for i, (problem_key, condition_key, promt) in enumerate(all_tasks):
        print(f"API CALL: {problem_key} -> {condition_key}...", end=" ", flush=True)

        response = client.chat.completions.create(
            model="gpt-5.5",
            reasoning_effort="none",
            max_completion_tokens=50,
            temperature=0.7,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": promt}
            ]
        )

        answer = response.choices[0].message.content.strip()
        print(f"-> {answer}", flush=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        writer.writerow([i + 1, "gpt-5.5", problem_key, condition_key, answer, timestamp])
        f.flush()
        count += 1

print(f"\nDone! {count} Answers saved.")
