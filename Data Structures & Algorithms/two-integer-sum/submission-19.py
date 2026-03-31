class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashIdx = {}

        for i in range(0, len(nums)):
            comp = target - nums[i]
            if comp in hashIdx:
                return [hashIdx[comp], i]
            hashIdx[nums[i]] = i
        return null 
        