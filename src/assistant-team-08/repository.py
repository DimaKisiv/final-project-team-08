# class for saving and updating records in file
import pickle
from constants import Paths, Messages
from collections import UserDict

class Saver:
    def __init__(self):
        self.__file_name = Paths.database_file

    def save(self, records):
        with open(self.__file_name, "wb") as f:
            pickle.dump(records, f)

    def load(self) -> list:
        try:
            with open(self.__file_name, "rb") as f:
                return pickle.load(f)
        except: 
            return {}
        

class Repository(UserDict):
    def __init__(self, saver: Saver):
        self.__saver = saver
        self.data = self.__saver.load()

    def get_all(self):
        return list(self.data.values())

    def add_record(self, name, record):
        self.data[name] = record
        self.__saver.save(self.data)
        pass

    def update_record(self, name, record):
        self.data[name] = record
        self.__saver.save(self.data)


    def delete_record(self, name):
        updated_records = []
        for record in self.records:
            if record.name.lower() != name.lower():
                updated_records.append(record)
        self.__saver.save(self.records)

    def find_by_name(self, name):
        name_lower = name.lower()
        for record in self.records:
            if record.name.lower() == name_lower:
                return record
        return Messages.ContactDoesNotExist
