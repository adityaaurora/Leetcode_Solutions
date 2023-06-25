#returns the longest common prefix from a list of strings eg strs = ["flow", "flower", "floating"]

class Solution(object):
    def longestCommonPrefix(self, strs):
        output = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return output
            output += strs[0][i]
        return output
