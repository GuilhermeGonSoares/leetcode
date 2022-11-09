class Solution(object):
    def maxProfit(self, prices):
        min_price, profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            l = prices[i] - min_price
            if l > profit:
                profit = l
        return profit

s = Solution()
print(s.maxProfit([7,6,1,3,1,]))


