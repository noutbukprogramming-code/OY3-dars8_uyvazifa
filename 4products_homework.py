import csv

umumiy = 0
with open("products_homework.csv", "r") as f:
    reader = csv.DictReader(f)
    print(f"{'name'}, {'price'}, {'quantity'}")
    for key in reader:
        qiymat = float(key["price"]) * int(key["quantity"])
        umumiy += qiymat
        print(f"{key['name']}, {'price'}, {'quantity'} {qiymat:.2f}")

