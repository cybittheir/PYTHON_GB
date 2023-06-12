# Задача 30:  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def fill_array(attr_array):
    
    first=int(attr_array[0])
    step=int(attr_array[1])
    size=int(attr_array[2])

    result=list()

    for i in range(size):
        result.append(first + i * step)
    return result

input_data=input("Введите первый элемент, шаг и количество элементов через пробел: ").split()

print (fill_array(input_data))