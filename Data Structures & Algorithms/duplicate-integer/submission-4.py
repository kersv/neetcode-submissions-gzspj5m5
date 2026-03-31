class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force
        # compare current value to the rest of the array return true if found a match
        for i in range(len(nums)-1): 
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        # return false if no matches were found
        return False
            
