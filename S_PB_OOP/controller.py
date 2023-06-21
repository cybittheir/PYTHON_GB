
from class_pb import PhoneBook
from view import Contact
from os.path import exists

import view

def start():
    view.clear()
    pb = PhoneBook('phones.txt')
    pb.init_base(pb.db_path)
    person = Contact()

    while True:
        choice = view.menu()
        match choice:
            case 1:
                person.show_contacts(pb.search_contact(view.input_search(view.search_query)))
            case 2:
                search_index = int(view.input_search(view.select_query).strip())
                old_lname = pb.contacts[search_index].last_name
                old_fname = pb.contacts[search_index].first_name

                person.show_contacts(pb.search_id(search_index))

                contact_change = person.input_changes(view.input_change_contact,search_index)
                pb.change_contact(search_index,contact_change)
 
                person.show_contacts(pb.search_id(search_index))
                view.print_message(view.contact_changed(contact_change.get('last_name') if contact_change.get('last_name') else old_lname, contact_change.get('first_name') if contact_change.get('first_name') else old_fname))

            case 3:
                search_index=int(view.input_search(view.select_query).strip())
                old_lname = pb.contacts[search_index].last_name
                old_fname = pb.contacts[search_index].first_name

                person.show_contacts(pb.search_id(search_index))
                pb.contacts.pop(search_index)

                view.print_message(view.contact_deleted(old_lname, old_fname))
            case 4:
                person.show_contacts(pb.contacts)
            case 5:
                pb.add_contact(person.input_contact(view.input_new_contact))
            case 6:
                pb.write_file(pb.db_path)
                pb.init_base(pb.db_path)
            case 7:
                pb.init_base(pb.db_path)
            case 0:
                view.print_message(view.normal_exit)
                break