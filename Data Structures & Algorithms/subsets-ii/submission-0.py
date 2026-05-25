class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # res 
        res = []

        nums.sort()
        # backtrack
        def backtrack(i, current):
            # base
            if i >= len(nums):
                res.append(current.copy())
                return

            # include
            current.append(nums[i])
            backtrack(i+1, current)

            # exclude
            current.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
                
            backtrack(i+1, current)        

        backtrack(0, [])
        return res