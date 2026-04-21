class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i = 0
        while i < len(prices):
            j = i + 1
            while j < len(prices):
                if prices[j] < prices[i]:
                    j += 1
                else:
                    profit = prices[j] - prices[i]
                    if profit > maxProfit:
                        maxProfit = profit
                    j += 1
            i += 1
        
        return maxProfit
                

        