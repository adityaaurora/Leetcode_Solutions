class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit_sum = 0
        digit_prod = 1
        digits = list(str(n))
        for i in range(len(digits)):
            digit_sum += int(digits[i])
            digit_prod = digit_prod * int(digits[i])
        return (digit_prod - digit_sum)
