class Record:
    def __init__(self, name):
        self.name = name
        self.email = ""
        pass
        #fields for:
        #id, name, address, phone numbers, email, birthday
    def __str__(self):
        str = f"Name: {self.name}, Email: {self.email}"
        return str

    #we should replace there methods with properties using proeprty() decorator

    def add_phone(self, phone):
        pass
    def remove_phone(self, phone):
        pass
    def set_address(self, address):
        pass
    def set_email(self, email):
        self.email = email
    def set_birthday(self, birthday):
        pass
    def find_phone(self, phone):
        pass