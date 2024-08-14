import re
from constants import errors 

phone_pattern = r"^\+?38[ _-]?\(?\d{3}\)?[ _-]?\d{3}[ _-]?\d{2}[ _-]?\d{2}$"
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
birthday_pattern = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$"

def validate_phone(phone):
  match = re.match(phone_pattern, phone)
  if match:
    return True
  print(errors['phone_not_valid'])
  return False

def validate_email(email):
  match = re.match(email_pattern, email)
  if match:
    return True
  print(errors['email_not_valid'])
  return False

def validate_birthday(birthday):
  match = re.match(birthday_pattern, birthday)
  if match:
    return True
  print(errors['birthday_not_valid'])
  return False
