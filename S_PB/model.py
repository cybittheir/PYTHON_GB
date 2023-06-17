import view
import os
from os.path import exists

phone_book = []

path = 'phones.txt'

clear = lambda: os.system('cls')

def init_base():
    phone_book.clear()
    if exists(path):
        open_file(path)
    else:
        write_file(path)
    if len(phone_book)==0:
        view.print_message(view.empty_file)
    else:
        view.print_message(view.open_successful(phone_book))

def open_file(path):
    with open(path, "r+", encoding = 'UTF-8') as file:
        data = file.readlines()
    if len(data)>0:
        for (i, contact) in enumerate(data):
            last_name, first_name, phone, comment, *_ = contact.strip().split('|')
            phone_book.append({'uid':i,'last_name':last_name,'first_name': first_name, 'phone':phone, 'comment': comment})

def write_file(path):
    with open(path, "w", encoding = 'UTF-8') as file:
        if len(phone_book)>0 :
            file.write(dict_to_str(phone_book))
            view.print_message(view.save_successful)
        else:
            file.write('')
            view.print_message(view.new_file)


def dict_to_str(book):
    result=""
    for contact in book:
        result += contact['last_name'].strip() + "|" + contact['first_name'].strip() + "|" + contact['phone'].strip() + "|" + contact['comment'].strip() + "\n"
    return result

def check_id():
    if len(phone_book)>0:
        uid_list = []
        for contact in phone_book:
            uid_list.append(int(contact.get('uid')))
        return {'uid': max(uid_list) + 1}
    else:
        return {'uid': 1}

def add_contact(new: dict):
    new.update(check_id())
    phone_book.append(new)
    view.print_message(view.contact_saved(new.get('last_name'),new.get('first_name')))

def search_contact(word: str) -> list[dict]:
    result=[]
    for contact in phone_book:
        for _, value in contact.items():
            if word.lower().strip() in str(value).lower().strip():
                result.append(contact)
    return result

def search_id(word: int) -> list[dict]:
    result=[]
    for contact in phone_book:
        if word == contact.get('uid'):
            result.append(contact)
            break
    return result

def change_contact(index: int, new: dict[str,str]):
    for key,field in new.items():
        if field != '' and field != 'uid':
            phone_book[index][key] = field


