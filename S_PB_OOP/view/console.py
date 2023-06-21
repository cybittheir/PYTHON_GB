from .text import *
import os

clear = lambda: os.system('cls')

def menu() -> int:

    print(main_menu)

    while True:
        choice = input(menu_choice)
        clear()
        if choice.isdigit() and 0 <= int(choice) < 8:
            return int(choice)
        print (input_error)

def input_search(message: str) -> str:
    return input(message)

def get_message_width(message: str) -> int:
    mess_list=message.split('\n')
    max = 0
    for st in mess_list:
        if max < len(st):
            max = len(st)
    return max

def print_message(message: str):
    length = get_message_width(message) + 1
    print ('\n' + '='*length)
    print (message)
    print ('='*length)

