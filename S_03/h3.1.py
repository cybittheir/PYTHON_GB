
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


##
#*Пример:*

#   5
#    1 2 3 4 5
#    3
#    -> 1
##

from random import randint

list_len = int(input("Введите длину списка: "))
max_num = int(input("Введите максимальное значение в списке: "))

new_list=list()

for i in range(list_len):
    new_list.append(randint(0,max_num))

print (new_list)

number = int(input("Введите целое число: "))

result=0

for i in range(len(new_list)):
    if number == new_list[i]:
        result+=1

if result > 0:
    print ("Число {} встречается в списке {} раз".format(number,result))
else:
    print ("В списке число {} не встречается ни разу".format(number))