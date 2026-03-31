class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1
        minVal = nums[left]
        while left < right:
            mid = (right + left) // 2
            
            if nums[mid] > nums[right] :
                minVal = min(minVal, nums[mid])
                left = mid +1
            else:
                minVal = min(minVal, nums[mid])
                right = mid
            
        return nums[left]