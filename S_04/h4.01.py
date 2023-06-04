# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 

# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.


from random import randint

len_1 = int(input("Введите длину первого множества: "))
len_2 = int(input("Введите длину второго множества: "))

new_list1=list()
new_list2=list()

for i in range(len_1):
    new_list1.append(randint(0,10))

for i in range(len_2):
    new_list2.append(randint(0,10))

print (new_list1)
print (new_list2)

result = list(set.intersection(set(new_list1),set(new_list2)))
result.sort()
for i in result:
    print (i, end=', ')

