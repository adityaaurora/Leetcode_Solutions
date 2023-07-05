class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        hashmap = {"X++" : 1, "++X" : 1, "X--" : -1, "--X" : -1}
        for char in operations:
            if char in hashmap:
                x += hashmap[char]
        return x
