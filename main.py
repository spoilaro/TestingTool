
def read_commands():
    parsed_lines = []

    with open("./broken-commands.txt", "r") as f:
        lines = f.readlines()
    for command in lines:
        command = command.replace("\n", "")
        parsed_lines.append(command)

    return parsed_lines


def main():
    broken_commands = read_commands()


if __name__ == "__main__":
    main()
