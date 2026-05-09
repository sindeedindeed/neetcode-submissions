class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for x in prices:
            if x < min_price:
                min_price = x
            diff = x - min_price
            if diff > max_profit:
                max_profit = diff

        return max_profit