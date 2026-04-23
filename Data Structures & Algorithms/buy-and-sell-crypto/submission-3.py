class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = prices[0]
        maxProfit = 0
        
        for i in range(0, len(prices)):
            minValue = min(prices[i], minValue)
            maxProfit = max(prices[i] - minValue, maxProfit)
            
        return maxProfit





                

        