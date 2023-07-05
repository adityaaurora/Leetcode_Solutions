class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_add = address.replace(".", "[.]")
        return new_add
