# Задание 44
#
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

print (lst)
table=[]

print ("\n***\n[", end = "")
for num in range(len(lst)):
    if lst[num] == 'robot':
        new = [1,0]
    elif lst[num] == 'human':
        new = [0,1]

    if (num < len(lst)-1):
        print (new,end=",\n")
    else:
        print (new,end="]\n")

    table.append(new)

print ("\n***\n", table)

