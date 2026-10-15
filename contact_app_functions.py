#functions will reside here

contacts = []
numbers = [1, 2, 3, 45]
print(numbers)
from random import randint

print(randint(1,50))

def create_contact(first_name, last_name, phone_number):
    for contact in contacts:
        if contact [-1] == phone_number:
            return None
    contact = [first_name, last_name, phone_number]
    contact.append([first_name, last_name, phone_number])
    contact.append(first_name)
    contact.append(last_name)
    contact.append(phone_number)
    contacts.append(contact)
    return contact
def clear_contacts():
    contacts.clear()
