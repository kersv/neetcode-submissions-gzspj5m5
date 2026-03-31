class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # TC = O(n^2), SC = O(1)
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        map = {}

        for num in nums:
            if map.get(num) == True:
                return True
            else:
                map[num] = True
        return False


