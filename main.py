from typing import List
from subprocess import run


def read_commands() -> List[str]:
    """Reads file of broken commands to a list."""
    parsed_lines = []

    with open("./broken-commands.txt", "r") as f:
        lines = f.readlines()
    for command in lines:
        command = command.replace("\n", "")
        parsed_lines.append(command)

    return parsed_lines


def command_runner():
    """Runs a list of commands given."""
    output = run("ls", capture_output=True).stdout


def main():
    """Main"""
    broken_commands = read_commands()

    command_runner()


if __name__ == "__main__":
    main()
