"""class for saving and updating records in file"""

from collections import UserDict
import pickle
from datetime import datetime, timedelta
from models import Note
from constants import Messages


class Saver:
    def __init__(self, path):
        self.__file_name = path

    def save(self, data):
        with open(self.__file_name, "wb") as f:
            pickle.dump(data, f)

    def load(self) -> list:
        try:
            with open(self.__file_name, "rb") as f:
                return pickle.load(f)
        except OSError:
            return {}


class AddressBook(UserDict):
    def __init__(self, saver: Saver):
        self.__saver = saver
        self.data = self.__saver.load()

    def get_all(self):
        return list(self.data.values())

    def add_record(self, name, record):
        self.data[name] = record
        self.__saver.save(self.data)

    def update_record(self, name, record):
        self.data[name] = record
        self.__saver.save(self.data)

    def get_upcoming_birthday(self, days):
        upcoming_birthdays = ""
        today = datetime.today().date()
        next_date = today + timedelta(days=int(days))

        for record in self.data.values():
            if record.birthday:
                birthday_in_datetime = datetime.strptime(
                    record.birthday.value, "%d.%m.%Y").date()
                birthday_this_year = birthday_in_datetime.replace(
                    year=today.year)
                if today <= birthday_this_year <= next_date:
                    if len(upcoming_birthdays) != 0:
                        upcoming_birthdays = upcoming_birthdays + '\n'
                    upcoming_birthdays = upcoming_birthdays + f"{record.name} {
                        Messages.UpcomingBirthdayMiddlePart} {birthday_this_year.strftime("%d.%m.%Y")}."

        if len(upcoming_birthdays) == 0:
            upcoming_birthdays = Messages.NoUpcomingBirthday

        return upcoming_birthdays

    def delete_record(self, name):
        del self.data[name]
        self.__saver.save(self.data)

    def find_by_name(self, name):
        return self.data.get(name)

    def find(self, field_name, value):
        for record in self.data.values():
            if field_name == "phone":
                if record.has_phone(value):
                    return record
            else:
                field = getattr(record, field_name, None)
                if field and field.value == value:
                    return record
        return None


class NotesBook(UserDict):
    def __init__(self, saver: Saver):
        self.__saver = saver
        self.data = self.__saver.load()

    def get_all(self):
        return list(self.data.values())

    def find_by_key(self, key) -> Note:
        return self.data.get(key)

    def find_by_tag(self, tag):
        return [n for n in self.get_all() if tag in n.tags]

    def add(self, key, note: Note):
        self.data[key] = note
        self.__saver.save(self.data)

    def update_note(self, key, note: Note):
        self.data[key] = note
        self.__saver.save(self.data)

    def delete_note(self, key):
        del self.data[key]
