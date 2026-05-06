import json
import random

QUESTIONS_FILE = "questions.json"


while True:
    with open(QUESTIONS_FILE,"r") as file:
        questions = json.load(file)
    reps = input(f"how long quiz has to be (max: {len(questions)}): ")
    try:
        reps = int(reps)
    except:
        print("wrong input")
        continue
    if reps not in range(1,len(questions)+1):
        print("wrong number")
        continue
    else:
        i=0
        points=0
        while i < reps:
            print(f"question: {i+1}/{reps}")
            question_number = random.randint(0,len(questions)-1)
            print(f'Q: {questions[question_number]["question"]}')
            for j in range(len(questions[question_number]["options"])):
                print(f'A: {questions[question_number]["options"][j]}')
            answer=input("answer: ")
            if answer.lower() == questions[question_number]["correct_answer"]:
                points+=1
                print("correct answer") 
            else:
                print("wrong answer")
            del questions[question_number]
            i+=1
        print(f"points: {points}/{reps}")
        input("press button to continue...")