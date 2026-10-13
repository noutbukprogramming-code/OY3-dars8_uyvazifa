import csv

name = input("Ism: ")
age = input("Yosh: ")
score = int(input("Ball: "))

if score >= 70:
    with open("new_students_homework.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, score])

    print("Student faylga qo'shildi.")
else:
    print("Ball 70 dan past. Fayl o'zgartirilmadi.")