import csv

count = 0
with open("books_homework.csv", "r") as f:
    print(f"{'title'}, {'author'}, {'year'}")

    reader = csv.DictReader(f)
    for key in reader:
        print(f"{key['title']}, {key['author']}, {key['year']}")
        if int(key["year"]) > 2021:
            count += 1
