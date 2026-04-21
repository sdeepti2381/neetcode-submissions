class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        maxProfit = 0

        for day, price in enumerate(prices):
            if price < cheapest:
                cheapest = price
            
            profit = price - cheapest
            if profit > maxProfit:
                maxProfit = profit
            
        
        return maxProfit

        