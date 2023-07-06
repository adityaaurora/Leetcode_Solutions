class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = 0
        output = []
        for i in range(len(nums)):
            running += nums[i]
            output.append(running)
        return output
