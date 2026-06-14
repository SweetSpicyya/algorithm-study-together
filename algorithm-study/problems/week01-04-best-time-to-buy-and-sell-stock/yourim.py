class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = prices[0]
        profit = 0
        for price in prices:
            if price < min:
                min = price
            max = price
            if profit < (max - min):
                profit = max - min

        return profit

##################################
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit