# Задание 44
#
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random

lst = ['robot'] * 10
lst += ['human'] * 10
lst += ['animal'] * 10
random.shuffle(lst)

print (lst)

def get_values(lst:list):
    sel = list(set(lst))
    select={}
    for i in range(len(sel)):
        convert = list()
        for x in range(len(sel)):
            if x == i:
                convert.append(1)
            else:
                convert.append(0)
        select[sel[i]] = list(convert)
        convert.clear()
    return select


def one_hot_convert(lst:list):
    print ("========")
    values=get_values(lst)
    print (values)

    table=[]
    print ("\n***\n[", end = "")
    for num in range(len(lst)):
        new = list(values[lst[num]])

        if (num < len(lst)-1):
            print (new,end=",\n")
        else:
            print (new,end="]\n")

        table.append(new)
    return table

print ("\n***\n", one_hot_convert(lst))

