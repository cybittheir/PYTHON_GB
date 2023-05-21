
# Найдите сумму цифр трехзначного числа.

print ("Введите трехзначное число:")
inNumber=input()

# способ 1
Number=int(inNumber)

summ1 = int(inNumber[0]) + int(inNumber[1]) + int(inNumber[2])

# способ 2
summ2 = 0

for i in range(len(inNumber)):
    summ2 += int(inNumber[i])

# способ 3
summ3 = Number//100 + (Number%100)//10 + (Number%100)%10

# выводим ответ

print (inNumber, "->", summ1, "("+inNumber[0], "+",inNumber[1], "+", inNumber[2]+")", summ2, summ3)
