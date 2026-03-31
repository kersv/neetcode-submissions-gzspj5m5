class Solution:
    def trap(self, height: List[int]) -> int:
        # return trapWater
        trapWater = 0

        # default maximum left and right heights, first height and last height
        leftMax, rightMax = height[0], height[-1]

        # 2 pointers start at left and right, 0 and end of array
        left, right = 0, len(height)-1

        # traverse through to find each water hold at each left 
        while left < right:

            if height[left] < height[right]:
                left+=1
                leftMax = max(leftMax, height[left])
                trapWater += leftMax - height[left]

            else: 
                right-=1
                rightMax = max(rightMax, height[right])
                trapWater += rightMax - height[right]

        
        return trapWater

