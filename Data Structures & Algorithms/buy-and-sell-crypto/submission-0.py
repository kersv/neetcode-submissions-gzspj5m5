class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        maxProfit = 0

        # left = buy, right = sell
        left = 0
        right = 1

        # loop through array until right reaches the end
        while right < len(prices):
            # profitable? 
            if prices[right] > prices[left]:
                currProfit = prices[right] - prices[left]
                maxProfit = max(maxProfit, currProfit)
            else:
                left = right
            right += 1
        
        return maxProfit
