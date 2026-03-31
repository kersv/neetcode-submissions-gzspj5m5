class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maxWater = 0

        # left = 0
        # right = len(heights)-1

        # while left < right:
        #     minHeight = min(heights[left], heights[right])
        #     width = right - left
        #     maxWater = max(maxWater, minHeight * width)

        #     left += 1
        #     right -= 1
        
        # return maxWater

        maxWater = 0

        for left in range(len(heights)):
            right = left +1
            while right != len(heights):
                minHeight = min(heights[left], heights[right])
                width = right - left
                maxWater = max(maxWater, minHeight * width)

                right += 1
        return maxWater

