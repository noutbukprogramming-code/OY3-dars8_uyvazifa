import csv

with open("inventory_homework.csv", "r") as file:
    reader = csv.DictReader(file)
    min_item = None

    for row in reader:
        if min_item == None or int(row["stock"]) < int(min_item["stock"]):
            min_item = row

if min_item:
    print(min_item["item"], min_item['category'], min_item['stock'])
    