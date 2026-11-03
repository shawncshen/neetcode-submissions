class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        i = 0
        r = 1
        while r < len(prices):
            if prices[i] <= prices[r]:
                profit = prices[r] - prices[i]
                max_profit = max(profit, max_profit)
                r+= 1
            elif prices[i] > prices[r]:
                i = r
                r += 1
        return max_profit


