# class for saving and updating records in file

from models.record import Record
from repository.saver import Saver


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