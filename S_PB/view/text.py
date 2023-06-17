main_menu='''
==================================
Главное меню
==================================
-> 1. Найти контакт
-> 2. Изменить контакт
-> 3. Удалить контакт
-> 4. Показать все контакты
-> 5. Создать контакт
-> 6. Сохранить файл справочника
-> 7. Перечитать файл справочника
-> 0. Выход
'''

menu_choice = 'Выберите пункт меню: '
input_error = 'Некорректный ввод! Введите от 0 до 7 включительно'
book_error = 'Телефонный справочник пуст или ошибка файла справочника'

input_new_contact = "Введите данные нового контакта"
input_change_contact = "Введите новые данные контакта"
empty_file = "Внимание!!!\nФайл справочника пуст.\nДобавьте первую запись -> 5"
save_successful = "Файл справочника успешно сохранен"
new_file = "Пустой файл справочника успешно создан"
normal_exit = "Спасибо за использование справочника"

all_records = "Всего записей: "
search_query = "Введите искомое слово или номер: "
select_query = "Введите ID контакта: "

fields={}
fields['last_name']='Введите фамилию контакта: '
fields['first_name'] = 'Введите имя контакта: '
fields['phone'] = 'Введите номер телефона: '
fields['comment'] = 'Введите комментарий: '

fields_name={}
fields_name['last_name']='Фамилия'
fields_name['first_name']='Имя'
fields_name['phone']='Телефон'
fields_name['comment']='Примечание'

fields_size={}
fields_size['last_name']=20
fields_size['first_name']=20
fields_size['phone']=13
fields_size['comment']=22

def open_successful(phone_book: list):
    return f'Файл справочника успешно прочитан\n{all_records}{len(phone_book)}'

def contact_saved(last_name: str, first_name: str):
    return f'Контакт {last_name} {first_name} добавлен.\nДля сохранения в файл -> 6\nДля отмены -> 7 (Перечитать файл справочника)'

def contact_changed(last_name: str, first_name: str):
    return f'Контакт {last_name} {first_name} изменен.\nДля сохранения изменений в файл -> 6\nДля отмены -> 7 (Перечитать файл справочника)'

def contact_deleted(last_name: str, first_name: str):
    return f'Контакт {last_name} {first_name} удален.\nДля сохранения изменений в файл -> 6\nДля отмены -> 7 (Перечитать файл справочника)'

def contact_error(last_name: str, first_name: str):
    return f'Ошибка! Контакт {last_name} {first_name} не добавлен в справочник'