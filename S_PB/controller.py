
from view import menu,show_contacts,input_contact,input_new_contact,open_successful,empty_file,print_message, normal_exit, input_search, search_query,select_query, contact_changed,input_change_contact,contact_deleted
# from model import open_file, print_message,input_contact
import model

def start():
    model.clear()
    model.init_base()

    while True:
        choice=menu()
        match choice:
            case 1:
                show_contacts(model.search_contact(input_search(search_query)))
            case 2:
                search_index = int(input_search(select_query).strip())
                old_lname = model.phone_book[search_index].get('last_name')
                old_fname = model.phone_book[search_index].get('first_name')

                show_contacts(model.search_id(search_index))

                contact_change = input_contact(input_change_contact,search_index)
                model.change_contact(search_index,contact_change)
 
                show_contacts(model.search_id(search_index))
                print_message(contact_changed(contact_change.get('last_name') if contact_change.get('last_name') else old_lname, contact_change.get('first_name') if contact_change.get('first_name') else old_fname))

            case 3:
                search_index=int(input_search(select_query).strip())
                old_lname = model.phone_book[search_index].get('last_name')
                old_fname = model.phone_book[search_index].get('first_name')

                show_contacts(model.search_id(search_index))
                model.phone_book.pop(search_index)

                print_message(contact_deleted(old_lname, old_fname))
            case 4:
                show_contacts(model.phone_book)
            case 5:
                model.add_contact(input_contact(input_new_contact, model.check_id()))
            case 6:
                model.write_file(model.path)
                model.init_base()
            case 7:
                model.init_base()
            case 0:
                print_message(normal_exit)
                break