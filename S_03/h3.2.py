
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

#    *Пример:*

#    5
#        1 2 3 4 5
#        6
#        -> 5
##

import math

from random import randint

list_len = int(input("Введите длину списка: "))
max_num = int(input("Введите максимальное значение в списке: "))

new_list=list()

for i in range(list_len):
    new_list.append(randint(0,max_num))

print (new_list, "(полный списко для контроля)")

short_list=list(set(new_list))

print(short_list, "(список уникальных элементов для контроля)")

number = int(input("Введите целое число: "))

diff=max_num
result=0
second_result=0

for i in range(len(short_list)):
    if abs(number - short_list[i]) < diff:
        diff = abs(number - short_list[i])
        result = short_list[i]
    elif abs(number - short_list[i]) == diff:
        second_result = short_list[i]

if abs(second_result-number)==abs(result-number):
    print ("Самые близкие к числу {} элементы списка равны {} и {}".format(number,result,second_result))    
else:
    print ("Самый близкий к числу {} элемент списка равен {}".format(number,result))
