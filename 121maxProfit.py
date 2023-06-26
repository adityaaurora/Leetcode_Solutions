#problem 121, prices is an unsorted array eg [7,1,5,3,6,4]. Output would be 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
class Solution(object):
    def maxProfit(self, prices):
        dif = 0
        temp_dif = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                temp_dif = prices[j] - prices[i]
                if temp_dif > dif:
                    dif = temp_dif
        return dif
