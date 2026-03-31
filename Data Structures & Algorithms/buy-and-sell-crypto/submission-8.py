class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # return default profit = 0
        profit = 0
        # left and right pointers, left, right = 0, 1
        left, right = 0, 1
        # while right does not equal len(prices) and left != right
        while left < right and right != len(prices):
            # if price[right] - price[left] < 0, slide left to right and right by 1
            if prices[right] - prices[left] < 0:
                left = right
                right +=1
            # else (it made a profit)
            else:
                # update profit = max(profit, currentProfit)
                profit = max(profit, prices[right] - prices[left])
                # move right pointer to next possible profit
                right +=1
        
        return profit

    # profit = 0
    # [10,1,5,6,7,1]
    # window
    # [10,1] = profit -9
    # [1,5] = profit 4
    # [1,5,6] = profit 5
    # [1,5,6,7] = profit 6
    # [1,5,6,7,1] = profit 0
    # right = end of arr