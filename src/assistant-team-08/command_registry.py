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
    return run_command


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
    return inner

# Define commands using the decorator


@register_command('add')
@input_error
def add_contact(args):
    """
    Command to add a contact with the given name and phone number to a storage
    """
    name, phone, *_ = args
    record = _repository.find_by_name(name)
    message = Messages.ContactUpdated
    if record is None:
        record = Record(name)
        _repository.add_record(name, record)
        message = Messages.ContactAdded
    if phone and record.find_phone(phone) is None:
        record.add_phone(phone)
    return message


@register_command('update_email')
def update_email(args):
    name, email, *_ = args
    if not _validator.validate_email(email):
        return Messages.EmailNotValid
    record = _repository.find_by_name(name)
    if record:
        record.email = email
        _repository.update_record(name, record)
    return Messages.ContactUpdated


@register_command('list')
def list_contacts(args):
    """
    Command to list all contacts.
    """
    contacts_string = "\n".join([str(record) for record in _repository.get_all()])
    return contacts_string

