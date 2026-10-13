import csv

score = []

with open("exam_results_homework.csv", "r") as file:
    reader = csv.DictReader(file)

    for key in reader:
        score.append(int(key["score"]))

    if score:
        print(f"{key['name']}, {max(score)}")
        print(f"{key['name']}, {min(score)}")
        print(f"{key['name']},{ sum(score) / len(score)}")

        count = 0

        for score in score:
            if score >= 70:
                count += 1

            print(f"{key['name']}, {count}")
    else:
        print("Natijalar mavjud emas.")