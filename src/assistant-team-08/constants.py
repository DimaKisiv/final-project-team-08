<<<<<<< HEAD
# fields with all available commands to keep them all in one place
import os
from pathlib import Path

=======
#fields with all available commands to keep them all in one place
import os
from pathlib import Path
>>>>>>> feature/notes

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
    NotesListEmpty = "Notes list is empty"
    BirthdayNotSet = "Birthday not set."
    UpcomingBirthdayMiddlePart = "has an upcoming birthday on"
    NoUpcomingBirthday = "You have no contacts with upcoming birthday"
    NoteAdded = "Note is successfully added"
    NoteUpdated = "Note is successfully updated"
    NoteDeleted = "Note is successfully deleted"
    NoteWithThisKeyNotExists = "Note with this key does not exist. Please provide correct key"
    NoteWithThisKeyAlreadyExists = "Note with this key already exists. Please provide unique key"
    ProvideKeyAndText = "To add a note please provide a unique key and text of the note"
    TagAlreadyExists = "This tag already exists at this note"
    TagDoesNotExist = "This tag does not exist at this note"
    TagAdded = "Tag added"
    TagDeleted = "Tag deleted"
    WrongKey = "Wrong key for note. Should be on alphanumeric value"
    WrongText = "You can't add empty note"
    WrongTag = "Wrong tag for note. Should be on alphanumeric value"

class Paths:
    addressbook_file = str(Path.home()) + os.sep + "addressbook.pkl"
    notesbook_file = str(Path.home()) + os.sep + "notesbook.pkl"