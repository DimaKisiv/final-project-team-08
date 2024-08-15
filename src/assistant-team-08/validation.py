import re


class Validation:
    PhonePattern = r"^\+?38[ _-]?\(?\d{3}\)?[ _-]?\d{3}[ _-]?\d{2}[ _-]?\d{2}$"
    EmailPattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    BirthdayPattern = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$"
    NamePattern = r"^[a-zA-Z-]+$"
    AddressPattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d, ]+$"

    def validate_phone(self, phone):
        match = re.match(self.PhonePattern, phone)
        if match:
            return True
        return False

    def validate_email(self, email):
        match = re.match(self.EmailPattern, email)
        if match:
            return True
        return False

    def validate_birthday(self, birthday):
        match = re.match(self.BirthdayPattern, birthday)
        if match:
            return True
        return False

    def validate_name(self, name):
        match = re.match(self.NamePattern, name)
        if match:
            return True
        return False

    def validate_address(self, address):
        match = re.match(self.AddressPattern, address)
        if match:
            return True
        return False
