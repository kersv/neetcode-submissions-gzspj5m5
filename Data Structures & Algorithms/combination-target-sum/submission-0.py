class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, current, total):
            # base case
            if total == target :
                res.append(current.copy())
                return

            # base case 2
            if i >= len(nums) or total > target:
                return

            # include
            current.append(nums[i])
            backtrack(i, current, total + nums[i])
            
            val = current.pop()
            # exclude
            backtrack(i+1, current, total)
            

        

        backtrack(0, [], 0)
        return res