class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        temp = 0
        for string in sentences:
            word_count = len(string.split())
            if word_count >= temp:
                temp = word_count
        return temp
