# class for saving and updating records in file

from models import Record


class Repository():
    records = list(Record)

    def __init__(self):
        self.__saver = Saver()

    def add_record(self, record):
        self.__saver.save(record)
        pass

    def update_record(self, record):
        #remove record from records in database
        #save
        pass

    def delete_record(self, id):
        pass
    
    def find_by_name(self, name):
        pass
        # filter by name Cache.records


class Saver:

    def __init__(self):
        self.__file_name = Paths.database_file


    def save(records):
        pass
        #save records to file

    def load(records):
        pass
        #load records from file
