# Assistant from Team-08

## Features
- **Add Contacts**:
  Add new contacts with name, phone number, email, and birthday.
- **Find Contacts**:
  Search for contacts by name, phone number, email, or birthday. Supports partial matching.
- **Edit Contacts**:
  Update existing contact details.
- **Delete Contacts**:
  Remove contacts from the contact book.
- **List All Contacts**:
  Display all contacts in the contact book.
- **Birthday Reminders**:
  List upcoming birthdays within a specified number of days.

*----Run the program: main.py----*
## Use the following commands within the program:

- Add a contact:
```
add <name> <phone_number> <email> <birthday>
```
- Find contact:
```
find <name|phone|email|birthday>
```
- Change a contact's phone number:
```
change <name> <old_phone_number> <new_phone_number>
```
- Show all contacts:
```
all
```
- Add a birthday to a contact:
```
add-birthday <name> <DD.MM.YYYY>
```
- Show a contact's birthday:
```
show-birthday <name>
```
- List upcoming birthdays:
```
birthdays
```
- Exit the program:
```
exit
```

## How It Works ##
- The program uses a command-line interface to interact with a contact book.
- Each command corresponds to a specific function, such as adding a new contact, finding contacts by name, phone number, email, or birthday, and displaying all contacts.
- The contact book is persisted between sessions using serialization. When the program is started, it loads the contact book from a file, and when the program is closed, it saves the contact book back to the file.