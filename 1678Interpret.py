class Solution:
    def interpret(self, command: str) -> str:
        new_command = command.replace("()","o")
        return new_command.replace("(al)","al")
