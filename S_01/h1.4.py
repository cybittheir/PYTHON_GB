
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


S = 60 

# S = (boy + boy) * 2 + boy + boy = 6 * boy => boy = S/6

boy = S//6

print (S, "->", boy, 4*boy, boy)