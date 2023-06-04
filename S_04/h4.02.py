# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

N = int(input("Какое количество кустов: "))

all_arr={}

for i in range(N):
    all_arr[i]=randint(5,40)

print (all_arr)

one_job={}
max = 1
best = 0

for i in range(N):
    if (i==0):
        one_job[i]= all_arr[N-1] + all_arr[i] + all_arr[i+1]
    elif (i == N-1):
        one_job[i]= all_arr[i-1] + all_arr[i] + all_arr[0]
    else:
        one_job[i] = all_arr[i-1] + all_arr[i] + all_arr[i+1]
    if (one_job[i] > max):
        max = one_job[i]
        best = i
    print (one_job[i])

print ("max = {}, best choice= {}".format(max,best+1)) # best + 1 -  для привычного порядка счёта кустов
