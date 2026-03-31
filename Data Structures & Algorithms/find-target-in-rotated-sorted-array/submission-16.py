class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans = mid
                return ans

            # check if left is sorted
            if nums[mid] >= nums[left]:
                if nums[mid] > target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid +1
            # right side sorted
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1




    
        return ans