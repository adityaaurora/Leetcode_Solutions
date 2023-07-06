class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = 0
        left = [0]
        right = []
        for i in range(len(nums)-1):
            left_sum += nums[i]
            left.append(left_sum)
        for i in range(len(nums)-1, 0, -1):
            right_sum += nums[i]
            right.append(right_sum)
            right.sort(reverse=True)
        right.append(0)
        return [abs(x-y) for x,y in zip(left,right)]
