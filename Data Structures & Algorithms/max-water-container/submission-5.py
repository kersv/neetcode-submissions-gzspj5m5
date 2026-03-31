class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        
        # goal find the area between two pointers

        # initialize maxWater
        maxWater = 0

        # initialize left and right, left being start of height array, right being end of height array
        left, right = 0, len(heights)-1
        # loop, find area by getting minimum height between two pointers (height) * indicies of right - left (width)
        while left < right:
            waterArea = min(heights[left], heights[right]) * (right - left)
            # check maxWater with max()
            maxWater = max(maxWater, waterArea)
            # move left pointer if left height is smaller than right, edge case if same height default to move left pointer
            if heights[left] <= heights[right]:
                left+=1
            # move right pointer if right height is smaller than left
            elif heights[right] < heights[left]:
                right-=1 

        # return maxWater
        return maxWater