import csv

with open("students_homework.csv", "r") as f:
    data = csv.DictReader(f)
    print(f"{'name'}, {'age'}, {'score'}")
    for key in data:
        if int(key["score"]) >= 85:
            print(f"{key['name']}, {key['age']}, {key['score']}")
