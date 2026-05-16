from problems import PROBLEMS
import random

def generate_task(iteration,seed):
    rng = random.Random(seed)
    tasks = []
    for i in range(iteration):
        for problems_key in PROBLEMS:
           condition_key = (rng.choice(list(PROBLEMS[problems_key]["conditions"].keys())))
           promt = PROBLEMS[problems_key]["conditions"][condition_key]
           tasks.append((problems_key,condition_key,promt))
    return tasks



