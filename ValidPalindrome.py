#concept: make a new string, iterate through each character in given string to check if it's alphanumeric
#use function isalnum() and if it is, then add the lower character to the new string 
#return true if string is the same forwards and backwards
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for char in s:
            if char.isalnum():
                new_str += char.lower()
        if new_str == new_str[::-1]:
            return True
