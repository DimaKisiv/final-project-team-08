from constants.messages import Messages
from helpers.parser import parse_input
from services.command_execution_service import CommandExecutionService
from constants.commands import Commands

def main():
    command_executor = CommandExecutionService()
    print(Messages.Wellcome)
    while True:
        command, *args = parse_input(input(Messages.EnterACommand))
        #validate command
        #call handler
        pass

if __name__ == "__main__":
    main()
