class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for i in range(0, len(prices)):
            j = i + 1
            while j < len(prices):
                maxProfit = max(maxProfit, prices[j] - prices[i])
                j += 1
            
        return maxProfit



                

        