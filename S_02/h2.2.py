
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import math

from random import randint

first,second = randint(0,1000),randint(0,1000)

summ = first + second
mult = first * second

print ("Сумма = {}, произведение = {}".format(summ,mult))

D=summ*summ-4*mult

f_answer = int((summ + int(float(D)**0.5))/2)
s_answer = int((summ - int(math.sqrt(D)))/2)

print (f_answer, s_answer, "??",  first, second)

stop_search = 0

for x in range(1000):
    for y in range(1000):
        if x + y == summ and x * y == mult:
            stop_search = 1
            break
    if stop_search == 1:
        break
print ("X = {}; Y = {}".format(x,y))

