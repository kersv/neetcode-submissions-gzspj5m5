class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TC = O(n) SC = O(1)
        profit = 0
        
        # left = buy, right = sell
        left = 0  
        right = 1

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])

            elif prices[left] > prices[right]:
                left = right
            
            right += 1
        return profit
            
        