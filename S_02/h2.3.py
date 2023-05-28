
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

quest=int(input("Введите целое число: "))

exp = 0
result = 1

while result <= quest:
    print ("2^{}={}".format(exp,result))
    result*=2
    exp+=1