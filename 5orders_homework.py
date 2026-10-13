import csv

jami = 0
soni = 0
with open("orders_homework.csv", "r") as f:
    reader = csv.DictReader(f)
    print(f"{'order_id'}, {'customer'}, {'amount'}")
    for key in reader:
        jami += int(key["amount"])
        soni += 1
        ortacha = jami / soni if soni else 0
        print(f"{key['order_id']}, {key['customer']}, {key['amount']}: Yig'indisi: {jami:.2f}")
        print(f"{key['order_id']}, {key['customer']}, {key['amount']}: O'rtacha qiymati: {ortacha:.2f}")