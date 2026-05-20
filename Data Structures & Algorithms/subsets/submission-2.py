class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, current):
            # base case
            if i >= len(nums):
                res.append(current.copy())
                return


            # decision 1 - include
            current.append(nums[i])
            backtrack(i+1, current)

            # backtrack 
            current.pop()

            # decision 2 - exclude
            backtrack(i+1, current)

        backtrack(0, [])
        return res