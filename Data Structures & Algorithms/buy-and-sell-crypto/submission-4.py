class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        # left = buy, right = sell
        left = 0  
        right = 1

        while right != len(prices):
            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
                right += 1
            elif prices[left] > prices[right]:
                left = right
                right = left + 1
            else:
                right += 1
        return profit
            
        