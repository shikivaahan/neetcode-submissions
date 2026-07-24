class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_seen = prices[0]
        profit = 0

        for price in prices:
            if price < min_seen:
                min_seen = price

            today_profit = price - min_seen

            if today_profit > profit:
                profit = today_profit
            
        return profit
        