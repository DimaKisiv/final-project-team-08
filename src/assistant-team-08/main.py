from constants import Messages
from parser import parse_input
from command_executor import CommandExecutionService
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
