class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashm:
                return [hashm[comp], i]
            hashm[nums[i]] = i
        return []
            