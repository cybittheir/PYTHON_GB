
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

quest=int(input("Введите количество монет: "))

num_list=[]
result=0

for i in range(quest):
    num_list.append(randint(0,1))

print(num_list)    

zero=0

for j in range(len(num_list)-1):
    if num_list[j] == 0:
        zero +=1

if zero==len(num_list)/2:
    print ("любые {}".format(zero))
elif zero<len(num_list)/2:
    print (zero, " орлов")
else:
    print(len(num_list)-zero, "решек")
