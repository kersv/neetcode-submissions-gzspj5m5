class Solution:
    def trap(self, height: List[int]) -> int:

        # return water
        water = 0

        # maxLeft and maxRight 
        maxLeft, maxRight = height[0], height[-1]
        # left and right pointer, start of height and end of height arr
        left, right = 0, len(height)-1

        while left < right:
            
            # check if height of left is less than right, move left pointer
            if height[left] < height[right]:

                left+=1
                maxLeft = max(maxLeft, height[left])
                water += (maxLeft - height[left])
            
            else:
                right-=1
                maxRight = max(maxRight, height[right])
                water += (maxRight - height[right])
            
        return water
        


        