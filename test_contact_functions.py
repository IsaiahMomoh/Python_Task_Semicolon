
from unittest import TestCase
from contact_app_functions import create_contact, clear_contacts
class TestContactApp(TestCase):

def test_that_newContact_canBeCreated_andSaved(self):
    clear_contacts()
    first_name = "Daniel"
    last_name = "Messiah"
    phone_number = "07062023537"

    contact = create_contact(first_name,last_name,phone_number)
    self.assertEqual(type(contact), list)
    self.assertEqual(len(contact), 3)
    self.assertEqual("07062023537", contact [-1])

def test_that_Duplicate_contacts_cannot_be_created(self):
    clear_contacts()
        first_name = "John"
        last_name = "James"
        phone_number = "07062023537"

        create_contact(first_name,last_name,phone_number)
        first_name = "Job"
        last_name = "Ann"
        phone_number = "07062023537"
        contact = create_contact(first_name,last_name,phone_number)
        self.assertIsNone(contact)


