class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = max(prices)
        profit = 0
        for x in prices:
            diff = abs(x - max_price)
            profit = diff if diff > profit else profit
        
        return profit