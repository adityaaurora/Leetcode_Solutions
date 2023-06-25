#prints the index of the target int in the int array 'nums'
class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
