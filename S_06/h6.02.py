# Задача 32: 
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def gen_array(min,max,size):
    return [randint(min,max) for _ in range(size)]

in_attr=input("Введите минимальный и максимальные элементы, и количество элементов через пробел: ").split()

min_first = int(in_attr[0])
max_first = int(in_attr[1])
size = int(in_attr[2])

in_array=[randint(min_first,max_first) for _ in range(size)]
print (in_array)

get_attr=input("Введите минимальный и максимальные элементы диапазона через пробел: ").split()

min_sel = int(get_attr[0])
max_sel = int(get_attr[1])
get_array={}

# for i in range(size):
#    if min_sel <= in_array[i] <= max_sel:
#        get_array[i]=in_array[i]

get_array=[{i,in_array[i]} for i in range(size) if min_sel <= in_array[i] <= max_sel]

print (get_array)
