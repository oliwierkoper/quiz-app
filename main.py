import json

QUESTIONS_FILE = "questions.json"

with open(QUESTIONS_FILE,"r") as file:
    questions = json.load(file)

while True:
    reps = input(f"how long quiz has to be (max: {len(questions)}): ")
    try:
        reps = int(reps)
    except:
        print("wrong input")
        continue
    if reps in range(1,len(questions)+1):
        print("ok")
    else:
        print("wrong number")