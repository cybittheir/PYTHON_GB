# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#

def example_exp(a, b):

    if (b > 1):
        return a * example_exp(a, b - 1)
    elif(b == 0):
        return 1
    return a

A = int(input("Введите число: "))
B = int(input("Введите степень числа: "))

print ("{}^{} = ".format(A,B) + str(example_exp(A,B)))

