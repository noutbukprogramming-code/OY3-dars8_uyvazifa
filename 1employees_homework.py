import csv

with open("employees_homework.csv", "r") as f:
    reader = csv.DictReader(f)
    print(f"{'name'}, {'department'}, {'salary'}")
    
    for key in reader:
        print(f"{key['name']}, {key['department']}, {key['salary']}")