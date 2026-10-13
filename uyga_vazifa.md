# Uyga vazifa: CSV fayllar bilan ishlash

Quyidagi 10 ta topshiriqni Python `csv` moduli yordamida bajaring. Har bir topshiriqda ko‘rsatilgan CSV fayl `vazifa` papkasida joylashgan. Fayllarda sarlavhadan tashqari 50 tadan ma’lumot qatori bor.

## Umumiy talablar

- Fayllarni `csv.DictReader` yoki `csv.reader` yordamida o‘qing.
- Sonli ustunlarni hisoblashdan oldin `int()` yoki `float()` ga o‘tkazing.
- Natijalarni konsolga aniq va tushunarli ko‘rinishda chiqaring.
- Yangi fayl yoziladigan topshiriqlarda ustun sarlavhalarini saqlang.

## 1. Xodimlar bo‘limi va maoshi

Fayl: `employees_homework.csv`

Vazifa: CSV faylni o‘qib, barcha xodimlarning ismi va bo‘limini konsolga chiqaring.

Namuna:

```csv
name,department,salary
Aziz Karimov,IT,3200
Madina Aliyeva,Marketing,3475
Sardor Rahimov,Moliya,3750
Nilufar Usmonova,Sotuv,4025
```

## 2. Yuqori natijali studentlar

Fayl: `students_homework.csv`

Vazifa: Balli 85 yoki undan yuqori bo‘lgan studentlarning ismi va ballini chiqaring.

Namuna:

```csv
name,age,score
Aziz Karimov,16,55
Madina Aliyeva,17,64
Sardor Rahimov,18,73
Nilufar Usmonova,19,82
```

## 3. Yangi kitoblar soni

Fayl: `books_homework.csv`

Vazifa: 2021-yildan keyin nashr etilgan kitoblar sonini aniqlang.

Namuna:

```csv
title,author,year
Python asoslari,A. Karimov,2018
Algoritmlar olami,M. Aliyeva,2019
Dasturlash sirlari,S. Rahimov,2020
Kitobxon kundaligi,N. Usmonova,2021
```

## 4. Ombordagi mahsulot qiymati

Fayl: `products_homework.csv`

Vazifa: Har bir mahsulot uchun price * quantity qiymatini hisoblang va barcha mahsulotlarning umumiy qiymatini toping.

Namuna:

```csv
name,price,quantity
Laptop,20,2
Mouse,57,3
Keyboard,94,4
Monitor,131,5
```

## 5. Buyurtmalar tahlili

Fayl: `orders_homework.csv`

Vazifa: Buyurtmalar summasi yig‘indisi va o‘rtacha buyurtma qiymatini hisoblang.

Namuna:

```csv
order_id,customer,amount
ORD-001,Aziz Karimov,120
ORD-002,Madina Aliyeva,203
ORD-003,Sardor Rahimov,286
ORD-004,Nilufar Usmonova,369
```

## 6. Eng kam qolgan mahsulot

Fayl: `inventory_homework.csv`

Vazifa: Omborda eng kam qolgan mahsulotning nomi va sonini toping.

Namuna:

```csv
item,category,stock
Laptop,Elektronika,3
Mouse,Kanselyariya,14
Keyboard,Oziq-ovqat,25
Monitor,Kiyim,36
```

## 7. Shartli ravishda student qo‘shish

Fayl: `new_students_homework.csv`

Vazifa: Foydalanuvchidan yangi studentning ismi, yoshi va ballini oling. Balli 70 yoki undan yuqori bo‘lsa, uni CSV fayl oxiriga qo‘shing; aks holda faylni o‘zgartirmang.

Namuna:

```csv
name,age,score
Student 1,16,60
Student 2,17,65
Student 3,18,70
Student 4,19,75
```

## 8. Aholisi katta shaharlar

Fayl: `cities_homework.csv`

Vazifa: Aholisi 500 000 dan ko‘p bo‘lgan shaharlar nomini chiqaring.

Namuna:

```csv
city,population
Toshkent,85000
Samarqand,222000
Namangan,359000
Andijon,496000
```

## 9. Katta xarajatlarni ajratish

Fayl: `expenses_homework.csv`

Vazifa: amount qiymati 200 dan katta bo‘lgan xarajatlarni yangi `large_expenses.csv` fayliga yozing. Yangi faylda `category` va `amount` ustunlari bo‘lsin.

Namuna:

```csv
category,amount
Elektronika,35
Kanselyariya,82
Oziq-ovqat,129
Kiyim,176
```

## 10. Imtihon natijalari

Fayl: `exam_results_homework.csv`

Vazifa: Eng yuqori ball, eng past ball, o‘rtacha ball va 70 yoki undan yuqori ball olganlar sonini aniqlang.

Namuna:

```csv
name,score
Aziz Karimov,48
Madina Aliyeva,61
Sardor Rahimov,74
Nilufar Usmonova,87
```

## Topshirish

Har bir masala uchun alohida `.py` fayl yarating. Dastur to‘g‘ri ishlashini berilgan CSV fayl bilan tekshiring.
