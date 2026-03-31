class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # # TC = O(n) SC = O(1)
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        map = {}

        for i,n in enumerate(nums):
            complement = target - n
            if complement in map:
                return [map[complement], i]
            else:
                map[n] = i
        return []
        
        