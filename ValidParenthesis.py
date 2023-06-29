'''concept:
make a stack, and a hashmap for all the closed parenthesis. 
iterate through every character in the string, check if it is a closed parenthesis.
If it is, and if the stack is not empty and the top value of the stack is an open parenthesis (using hash), then remove the top value.
If not then return false
However, if the string has open parenthesis, then add them to the stack. Stack should only have open parenthesis values.
eventually if it is a valid parenthesis, then the stack would be empty because if it wasn't a valid string then it wouldn't pop a value.
If it is empty then return true '''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
