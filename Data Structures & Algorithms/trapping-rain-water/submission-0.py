class Solution:
    def trap(self, height: List[int]) -> int:
        sumOfWater = 0
        maxLeft = height[0]
        maxRight = height[len(height)-1]
        
        left = 0
        right = len(height)-1
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                sumOfWater += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                sumOfWater += maxRight - height[right]
        
        return sumOfWater
            
            



        