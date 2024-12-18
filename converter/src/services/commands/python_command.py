from src.services.commands.command import Command
from src.common.exceptions.command_exception import CommandException


class PythonCommand(Command):

    def __init__(self):
        self.name = "python"

    def build(self, parameter):
        parameter.validate()
        try:
            python_compiler = parameter.get_binary() + 'python '
            cmd = python_compiler + parameter.get_file_path()
            return cmd
        except Exception as error:
            raise CommandException("Python command error")
