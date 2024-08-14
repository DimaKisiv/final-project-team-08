from constants import Messages
from parser import parse_input
import command_registry as command_service


def main():
    print(Messages.Wellcome)
    # TODO replace dict with repository
    # TODO load storage from the file
    storage = {}
    command_executor = command_service.create_command_executor(storage)
    while True:
        command, *args = parse_input(input(Messages.EnterACommand))
        print(command_executor(command, *args))
        # TODO save storage to the file


if __name__ == "__main__":
    main()
