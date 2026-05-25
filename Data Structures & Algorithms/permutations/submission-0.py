class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []


        def backtrack(current):
            # base case
            if len(current) == len(nums):
                res.append(current.copy())
                return

            for num in nums:
                if num in current:
                    continue
            
                # include
                current.append(num)
                backtrack(current)

                # exclude
                current.pop()

        backtrack([])
        return res