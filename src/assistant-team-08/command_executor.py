#class for handlingn all commands
from constants.commands import Commands
from repository import Saver
from repository import Repository

class CommandExecutionService():
    def __init__(self):
        self.__repository = Repository()
        self.__save = Saver()

    def parse_input(self, command):
        pass
    
    def execute_command(self, command):
        #create command executor
        #run command
        pass

    def add_contact(self, record):
        #check if already exists
        self.__repository.add_record(record)

    def update_contact():
        pass

    def search_by_name():
        pass     
    #some other required methods
