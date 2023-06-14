# Задача 34:  
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

good = "Парам пам-пам"
bad = "Пам парам"
words=0
vowel_chr="|"

get_input=input("Введите рифму: ").strip().split()

vowels=("а","е","ё","и","о","у","э","ю","я")

def some_replace(in_string,val_array=vowels,val_change=vowel_chr):
    result=in_string
    for i in val_array:
        if i in in_string:
            result=result.replace(i,val_change)
    return result

for sel_string in get_input:
    arr_words=some_replace(sel_string).strip().split(vowel_chr)
    if words == 0:
        words = len(arr_words)
    elif words == len(arr_words):
        result = good
    else: 
        result = bad

print (result)