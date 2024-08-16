"""test suit for commands"""
from datetime import datetime
import unittest
from unittest.mock import MagicMock
import command_registry as command_service
from constants import Messages, Paths
from repository import AddressBook, Saver


class TestCommand(unittest.TestCase):

    def setUp(self):
        self.saver = Saver(Paths.addressbook_file)
        self.saver.load = MagicMock(return_value={})
        self.saver.save = MagicMock()
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()

    def test_non_existing_command(self):
        command_service._addressbook = AddressBook(self.saver)
        result = self.command_executor("noneExistingCommand")
        self.assertEqual(
            result, Messages.InvalidCommand)

    def test_add_command_with_no_enough_args(self):
        command_service._addressbook = AddressBook(self.saver)
        result = self.command_executor("add_contact")
        self.assertEqual(
            result, Messages.WrongParameters)

    def test_add_command_with_wrong_number(self):
        command_service._addressbook = AddressBook(self.saver)
        result = self.command_executor("add_contact", "John", "12422424")
        self.assertEqual(
            result, Messages.WrongPhoneNumber)

    def test_add_command_with_name_and_correct_number(self):
        command_service._addressbook = AddressBook(self.saver)
        result = self.command_executor("add_contact", "John", "+380981171922")
        self.assertEqual(result, Messages.ContactAdded)

    def test_add_command_when_contact_already_existing(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor("add_contact", "John", "+380981171922")
        self.assertEqual(result, Messages.ContactAlreadyExists)

    def test_add_command_when_name_is_wrong(self):
        command_service._addressbook = AddressBook(self.saver)
        result = self.command_executor("add_contact", "1111", "+380981171922")
        self.assertEqual(result, Messages.WrongNameValue)

    def test_add_phone_to_existing_contact(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor("add_phone", "John", "+380987654321")
        self.assertEqual(result, Messages.PhoneAdded)

    def test_add_phone_when_phone_is_wrong(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        result = self.command_executor(
            "add_phone", "John", "+3809876543211222")
        self.assertEqual(result, Messages.WrongPhoneNumber)

    def test_add_phone_to_non_existing_contact(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        result = self.command_executor("add_phone", "John", "+380987654321")
        self.assertEqual(result, Messages.ContactDoesNotExist)

    def test_update_phone_with_wrong_old_number(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor(
            "update_phone", "John", "+38098117192234", "+380987654321")
        self.assertEqual(result, Messages.WrongPhoneNumber)

    def test_update_phone_with_wrong_new_number(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor(
            "update_phone", "John", "+380981171922", "+38098765432122")
        self.assertEqual(result, Messages.WrongPhoneNumber)

    def test_update_phone_when_contact_does_not_exist(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        result = self.command_executor(
            "update_phone", "John", "+380981171922", "+380987654321")
        self.assertEqual(result, Messages.ContactDoesNotExist)

    def test_update_phone_in_existing_contact(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor(
            "update_phone", "John", "+380981171922", "+380987654321")
        self.assertEqual(result, Messages.ContactUpdated)

    def test_update_phone_when_old_phone_does_not_exist(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor(
            "update_phone", "John", "+380000000000", "+380987654321")
        self.assertEqual(result, Messages.GiveNameWithOldAndNewPhones)

    def test_update_email_in_existing_contact(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor(
            "update_email", "John", "john@example.com")
        self.assertEqual(result, Messages.ContactUpdated)

    def test_update_email_when_email_is_wrong(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor(
            "update_email", "John", "johnexample.com")
        self.assertEqual(result, Messages.EmailNotValid)

    def test_update_email_when_contact_does_not_exist(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        result = self.command_executor(
            "update_email", "John", "johne@xample.com")
        self.assertEqual(result, Messages.ContactDoesNotExist)

    def test_update_address_in_existing_contact(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor("update_address", "John", "123 Main St")
        self.assertEqual(result, Messages.ContactUpdated)

    def test_update_address_when_address_is_wrong(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor("update_address", "John", "122")
        self.assertEqual(result, Messages.WrongAddress)

    def test_update_address_contact_does_not_exist(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        result = self.command_executor("update_address", "John", "123 Main St")
        self.assertEqual(result, Messages.ContactDoesNotExist)

    def test_update_birthday_when_birthday_is_wrong(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor("update_birthday", "John", "01.27.2000")
        self.assertEqual(result, Messages.BirthdayNotValid)

    def test_update_birthday_in_existing_contact(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor("update_birthday", "John", "01.01.2000")
        self.assertEqual(result, Messages.ContactUpdated)

    def test_show_birthday_for_contact(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        self.command_executor("update_birthday", "John", "01.01.2000")
        result = self.command_executor("show_birthday", "John")
        self.assertEqual(result.value, "01.01.2000")

    def test_show_birthday_for_contact_with_no_birthday(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor("show_birthday", "John")
        self.assertEqual(result, Messages.BirthdayNotSet)

    def test_show_upcoming_birthday(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        self.command_executor("update_birthday", "John",
                              datetime.today().strftime("%d.%m.%Y"))
        result = self.command_executor("show_upcoming_birthday", "7")
        self.assertIn(Messages.UpcomingBirthdayMiddlePart, result)

    def test_delete_contact(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor("delete", "John")
        self.assertEqual(result, Messages.ContactDeleted)

    def test_delete_when_contact_does_not_exist(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        result = self.command_executor("delete", "John")
        self.assertEqual(result, Messages.ContactDoesNotExist)

    def test_find_contact_by_name(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor("find_contact", "John")
        self.assertIn("John", str(result))

    def test_find_contact_by_phone(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor("find_contact", "+380981171922")
        self.assertIn("John", str(result))

    def test_find_contact_by_email(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        self.command_executor("update_email", "John", "john@example.com")
        result = self.command_executor("find_contact", "john@example.com")
        self.assertIn("John", str(result))

    def test_find_contact_by_birthday(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        self.command_executor("update_birthday", "John", "01.01.2000")
        result = self.command_executor("find_contact", "01.01.2000")
        self.assertIn("John", str(result))

    def test_find_contact_by_non_existent_name(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        result = self.command_executor("find_contact", "NonExistentName")
        self.assertEqual(result, Messages.ContactDoesNotExist)

    def test_list_when_there_are_no_contacts(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        self.command_executor("add_contact", "John", "+380981171922")
        result = self.command_executor("list_addressbook")
        self.assertIn("John", str(result))

    def test_list_is_not_empty_when_contacts_exist(self):
        command_service._addressbook = AddressBook(self.saver)
        self.command_executor = command_service.create_command_executor()
        result = self.command_executor("list_addressbook")
        self.assertEqual(result, Messages.ContactListEmpty)

    def test_get_commands_is_not_empty(self):
        self.assertNotEqual(len(command_service.get_commands()), 0)


if __name__ == '__main__':
    unittest.main()
