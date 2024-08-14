import re
from constants import Messages

class Validation:
  PhonePattern = r"^\+?38[ _-]?\(?\d{3}\)?[ _-]?\d{3}[ _-]?\d{2}[ _-]?\d{2}$"
  EmailPattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
  BirthdayPattern = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$"

  def validate_phone(self, phone):
    match = re.match(self.PhonePattern, phone)
    if match:
      return True
    print(Messages.PhoneNotValid)
    return False

  def validate_email(self, email):
    match = re.match(self.EmailPattern, email)
    if match:
      return True
    print(Messages.EmailNotValid)
    return False

  def validate_birthday(self, birthday):
    match = re.match(self.BirthdayPattern, birthday)
    if match:
      return True
    print(Messages.BirthdayNotValid)
    return False