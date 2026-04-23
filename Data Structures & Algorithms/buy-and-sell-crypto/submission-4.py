class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = prices[0]
        maxProfit = 0
        
        for price in prices:
            minValue = min(price, minValue)
            maxProfit = max(price - minValue, maxProfit)
            
        return maxProfit





                

        