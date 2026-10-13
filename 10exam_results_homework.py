import csv

with open("exam_results_homework.csv", "r") as file:
    reader = csv.DictReader(file)
    students = list(reader)

if students:
    scores = [int(student["score"]) for student in students]

    highest = max(students, key=lambda student: int(student["score"]))
    lowest = min(students, key=lambda student: int(student["score"]))
    average = sum(scores) / len(scores)

    print("Eng yuqori ball:")
    print("name,score")
    print(highest["name"], highest["score"])

    print("\nEng past ball:")
    print("name,score")
    print(lowest["name"], lowest["score"])

    print("\nO'rtacha ball:", average)

    print("\n70 yoki undan yuqori ball olganlar:")
    print("name,score")

    for student in students:
        if int(student["score"]) >= 70:
            print(student["name"], student["score"])