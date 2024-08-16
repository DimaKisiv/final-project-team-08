# fields with all available commands to keep them all in one place
import os
from pathlib import Path


class Messages:
    Welcome = "Welcome to the assistant bot!"
    EnterACommand = "Enter a command: "
    HowCanIHelpYou = "How can I help you?"
    InvalidCommand = "Invalid command."
    WrongParameters = "Wrong parameters"
    WrongPhoneNumber = "wrong phone number. Must be 12 numbers starting with 38"
    WrongAddress = "Wrong address. Only allowed letters, numbers, comas and spaces"
    WrongBirthdayValue = "Wrong birthday value, should be DD.MM.YYYY"
    WrongNameValue = "Wrong name value. Should contain only letters and hyphens."
    ContactDoesNotHaveBirthdayValue = "Contact does not have birthday value"
    EnterUserName = "Enter user name"
    GiveNameAndPhone = "Give me name and phone please."
    GiveNameWithOldAndNewPhones = "Give me name with old and new phones please."
    ContactAlreadyExists = "Contact already exists"
    ContactDoesNotExist = "Contact does not exist"
    ContactUpdated = "Contact updated."
    ContactAdded = "Contact added."
    PhoneAdded = "Phone added."
    PhoneAlreadyExists = "Phone already exists."
    ContactDeleted = "Contact deleted."
    BirthdayAdded = "Birthday added."
    GoodBye = "Good bye!"
    PhoneNotValid = "Invalid phone number format"
    EmailNotValid = "Invalid email format"
    BirthdayNotValid = "Invalid date format. Use DD.MM.YYYY"
    ContactListEmpty = "Contact list is empty"
    BirthdayNotSet = "Birthday not set."
    UpcomingBirthdayMiddlePart = "has an upcoming birthday on"
    NoUpcomingBirthday = "You have no contacts with upcoming birthday"


class Paths:
    # Path to the database file in user's home directory
    database_file = str(Path.home()) + os.sep + "data.pkl"
