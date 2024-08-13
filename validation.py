import re
from errors import errors 

phone_pattern = r"^\+?38[ _-]?\(?\d{3}\)?[ _-]?\d{3}[ _-]?\d{2}[ _-]?\d{2}$"
email_patter = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

def validate_phone(phone):
  match = re.match(phone_pattern, phone)
  if match:
    return True
  print(errors['phone_not_valid'])
  return False

def validate_email(email):
  match = re.match(email_patter, email)
  if match:
    return True
  print(errors['email_not_valid'])
  return False