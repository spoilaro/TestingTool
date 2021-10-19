from typing import List
from subprocess import Popen, PIPE
import unittest


class TestingTool(unittest.TestCase):

    def read_commands(self, file_name: str) -> List[str]:
        """Reads file of broken commands to a list."""
        parsed_lines = []

        with open(f"./{file_name}", "r") as f:
            lines = f.readlines()
        for command in lines:
            command = command.replace("\n", "")
            parsed_lines.append(command)

        return parsed_lines

    def test_commands(self):
        """Runs a list of commands given."""
        broken_commands = self.read_commands("broken-commands.txt")
        correct_commands = self.read_commands("correct-commands.txt")

        for command_indx in range(len(broken_commands)):
            p = Popen(
                [f"thefuck -y {broken_commands[command_indx]}"], stdout=PIPE, shell=True)
            stdout, _ = p.communicate()

            res_str = stdout.decode("utf-8")
            correct_str = correct_commands[command_indx]

            self.assertEqual(res_str, correct_str)


def main():
    """Main"""
    tester = TestingTool()

    broken_commands = tester.read_commands("broken-commands.txt")
    correct_commands = tester.read_commands("correct-commands.txt")

    tester.command_runner(broken_commands, correct_commands)


if __name__ == "__main__":
    unittest.main()
