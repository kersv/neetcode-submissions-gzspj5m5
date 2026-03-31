class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {}

        for idx,val in enumerate(nums):
            diff = target - val
            if diff in idxMap:
                return [idxMap[diff], idx]
            idxMap[val] = idx
        