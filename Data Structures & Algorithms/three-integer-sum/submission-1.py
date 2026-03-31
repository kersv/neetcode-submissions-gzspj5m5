class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [2,-5,-3,0,3,-5]
        # [-5,-5,-3,0,2,3] Sorted        
        # create array to return values
        ans = []
        # sort the array 
        nums.sort()

        # loop through the array 
        for i, a in enumerate(nums):
            # skip the same element to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue
            
            # get left and right pointers of the current iteration 
            left = i + 1
            right = len(nums) - 1
            # while left < right calculate the three values and move pointers if greater or less than 0
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1 
                else:
                    # if threeSum equal 0 append to ans array 
                    ans.append([a, nums[left], nums[right]])
                    # move pointers to the next different number
                    left += 1 
                    right -= 1

                    # increment left again if its the same value as previous index
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        
        # return answer
        return ans
        
