from .text import *
from model import clear

def menu() -> int:

    print(main_menu)

    while True:
        choice = input(menu_choice)
        clear()
        if choice.isdigit() and 0 <= int(choice) < 8:
            return int(choice)
        print (input_error)

def show_contacts(book: list[dict[str,str]]):
    if book:
        print('\n' + '='*90)
        print(f'| {"ID":>3} | {fields_name["last_name"]:<{fields_size["last_name"]}}| {fields_name["first_name"]:<{fields_size["first_name"]}}| {fields_name["phone"]:<{fields_size["phone"]}}| {fields_name["comment"]:<{fields_size["comment"]}}|')
        print('='*90)
        for contact in book:
            uid, last_name, first_name, phone, comment = contact.values()
            print(f'| {uid:>3} | {last_name:<{fields_size["last_name"]}}| {first_name:<{fields_size["first_name"]}}| {phone:<{fields_size["phone"]}}| {comment:<{fields_size["comment"]}}|')
        print('='*90)
        print(f'{all_records} {len(book)}')
    else:
        print (book_error)

def print_message(message: str):
    length = get_message_width(message) + 1
    print ('\n' + '='*length)
    print (message)
    print ('='*length)

def input_contact(message: str,uid: int) -> dict[str,str]:
    print_message(message)
    last_name = input (fields['last_name'])
    first_name = input (fields['first_name'])
    phone = input (fields['phone'])
    comment = input (fields['comment'])
    return {'uid': uid,'last_name': last_name,'first_name': first_name, 'phone': phone, 'comment': comment}

def input_search(message: str) -> str:
    return input(message)

def get_message_width(message: str) -> int:
    mess_list=message.split('\n')
    max = 0
    for st in mess_list:
        if max < len(st):
            max = len(st)
    return max

