class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashm = {}
        for i in range(len(nums)):
            hashm[nums[i]] = hashm.get(nums[i], 0) +1
            if hashm[nums[i]] > 1:
                return True
        return False
        
        