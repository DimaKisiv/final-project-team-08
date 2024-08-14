#fields with all available commands to keep them all in one place

class Commands:
    pass

#fields with texts for user to keep them all in one place
class Messages:
    Wellcome = "Welcome to the assistant bot!"
    EnterACommand = "Enter a command: "
    HowCanIHelpYou = "How can I help you?"
    InvalidCommand = "Invalid command."
    WrongParameters = "Wrong parameters"
    WrongPhoneNumber = "wrong phone number"
    WrongBirthdayValue = "Wrong birthday value, should be DD.MM.YYYY"
    ContactDoesNotHaveBirthdayValue = "Contact does not have birthday value"
    EnterUserName = "Enter user name"
    GiveNameAndPhone = "Give me name and phone please."
    GiveNameWithOldAndNewPhones = "Give me name with old and new phones please."
    ContactAlreadyExists = "Contact already exists"
    ContactDoesNotExist = "Contact does not exist"
    ContactChanged = "Contact changed."
    ContactAdded = "Contact added."
    PhoneAdded = "Phone added."
    PhoneAlreadyExists = "Phone already exists."
    ContactDeleted ="Contact deleted."
    BirthdayAdded ="Birthday added."
    GoodBye = "Good bye!"

class Paths:
    database_file = "repository/data.txt"
