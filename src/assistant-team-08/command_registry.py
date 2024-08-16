"""
This module provides a simple command execution framework using a registry of commands.
Commands can be registered with the `register_command` decorator and then executed
through the `create_command_executor` function.

Usage:
1. Define commands using the `@register_command('command_name')` decorator.
2. Create a command executor using `create_command_executor()`.
3. Call the executor with the command string and arguments to execute the registered command.

Example:
    @register_command('add')
    def add_contact(name, phone):
        print(f"Adding contact: {name} with phone {phone}")

    @register_command('list')
    def list_contacts():
        print("Listing all contacts")

    command_executor = create_command_executor({})
    command_executor("add", "John", "+38098442123")
    command_executor("list")
"""
from models import Record
from constants import Messages
from repository import Repository, Saver
from validation import Validation

_command_registry = {}
_saver = Saver()
_repository = Repository(_saver)
_validator = Validation()


def create_command_executor():
    """
    Creates and returns a command executor function.
    """
    def run_command(command_str: str, *args):
        """Executes a command based on the command string."""
        command_func = _command_registry.get(command_str.lower())
        if command_func:
            return command_func(args)
        else:
            return Messages.InvalidCommand
    return run_command


def get_commands():
    """returns the list of the existing commands"""
    return list(_command_registry.keys())


def register_command(name):
    """
    Decorator to register a command function.
    """
    def decorator(func):
        # Register the function in the command_registry dictionary
        _command_registry[name.lower()] = func
        return func
    return decorator


def input_error(func):
    """
    Decorator for handling input error
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error: Command requires exactly 2 arguments (name and phone/birthday/address)."
        except KeyError:
            return "Error: No contact with this name was found in the dictation"
        except IndexError:
            return "Error: Command requires 1 argument (name)"
        except Exception as e:
            return f"Unexpected Error: {str(e)}"
    return inner

# Define commands using the decorator


@register_command('add')
@input_error
def add_contact(args):
    """
    Command to add a contact with the given name and phone number to a storage
    """
    name, phone, *_ = args
    email = args[2] if len(args) > 2 else None
    address = args[3] if len(args) > 3 else None
    birthday = args[4] if len(args) > 4 else None

    if not _validator.validate_name(name):
        return Messages.WrongNameValue
    if not _validator.validate_phone(phone):
        return Messages.WrongPhoneNumber
    record = _repository.find_by_name(name)
    if record is not None:
        return Messages.ContactAlreadyExists
    record = Record(name)
    record.add_phone(phone)
    _repository.add_record(name, record)
    if email and _validator.validate_email(email):
        record.email = email
        _repository.update_record(name, record)
    
    if address and _validator.validate_address(address):
        record.address = address
        _repository.update_record(name, record)
            
    if birthday and _validator.validate_birthday(birthday):
        record.birthday = birthday
        _repository.update_record(name, record)

    return Messages.ContactAdded

@register_command('add_phone')
@input_error
def add_phone(args):
    name, phone, *_ = args
    if not _validator.validate_phone(phone):
        return Messages.WrongPhoneNumber
    record = _repository.find_by_name(name)
    if record is None:
        return Messages.ContactDoesNotExist
    record.add_phone(phone)
    _repository.update_record(name, record)
    return Messages.PhoneAdded

@register_command('update_phone')
@input_error
def update_phone(args):
    name, old_phone, new_phone, *_ = args
    if not _validator.validate_phone(old_phone):
        return Messages.WrongPhoneNumber
    if not _validator.validate_phone(new_phone):
        return Messages.WrongPhoneNumber
    record = _repository.find_by_name(name)
    if record is None:
        return Messages.ContactDoesNotExist
    if not record.has_phone(old_phone):
        Messages.GiveNameWithOldAndNewPhones
    record.remove_phone(old_phone)
    record.add_phone(new_phone)
    _repository.update_record(name, record)
    return Messages.ContactUpdated

@register_command('update_email')
@input_error
def update_email(args):
    name, email, *_ = args
    if not _validator.validate_email(email):
        return Messages.EmailNotValid
    record = _repository.find_by_name(name)
    if record is None:
        return Messages.ContactDoesNotExist
    record.email = email
    _repository.update_record(name, record)
    return Messages.ContactUpdated

@register_command('update_address')
@input_error
def update_address(args):
    name, address, *_ = args
    if not _validator.validate_address(address):
        return Messages.WrongAddress
    record = _repository.find_by_name(name)
    if record is None:
        return Messages.ContactDoesNotExist
    record.address = address
    _repository.update_record(name, record)
    return Messages.ContactUpdated

@register_command('update_birthday')
@input_error
def update_birthday(args):
    name, date, *_ = args
    if not _validator.validate_birthday(date):
        return Messages.BirthdayNotValid
    record = _repository.find_by_name(name)
    if record:
        record.birthday = date
        _repository.update_record(name, record)
    return Messages.ContactUpdated

@register_command('show_birthday')
@input_error
def show_birthday(args):
    name, *_ = args
    record = _repository.find_by_name(name)
    if record and record.birthday:
        return record.birthday
    return Messages.BirthdayNotSet

@register_command('show_upcoming_birthday')
def show_upcoming_birthday(args):
    days, *_ = args or [7]
    return _repository.get_upcoming_birthday(days)

@register_command('list')
def list_contacts(args):
    """
    Command to list all contacts.
    """
    contacts_string = "\n".join([str(record) for record in _repository.get_all()])

    if not contacts_string:
        return Messages.ContactListEmpty

    return contacts_string

@register_command('delete')
@input_error
def delete_contact(args):
    """
    The command to delete a contact by name
    """
    name, *_ = args
    record = _repository.find_by_name(name)
    if record is None:
        return Messages.ContactDoesNotExist

    _repository.delete_record(name)
    return Messages.ContactDeleted

@register_command('find')
@input_error
def find_contact(args):
    """
    The command to find a contact by name, phone, email or birthday
    """
    value, *_ = args
    record = _repository.find_by_name(value)
    if record is not None:
        return record

    if _validator.validate_phone(value):
        record = _repository.find("phone", value)

    if _validator.validate_email(value):
        record = _repository.find("email", value)

    if _validator.validate_birthday(value):
        record = _repository.find("birthday", value)

    return str(record) or Messages.ContactDoesNotExist
