import csv

with open("cities_homework.csv", "r") as f:
    reader = csv.DictReader(f)
    print(f"{'city'}, {'population'}")
    for key in reader:
        if int(key['population']) > 500000:
            print(f"{key['city']}, {key['population']}")