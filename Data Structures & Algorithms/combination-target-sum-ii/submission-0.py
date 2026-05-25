class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # result list
        res = []

        # sort canidates
        candidates.sort()

        print(candidates)
        # backtrack function
        def backtrack(i, current, total):
            # base case
            if total == target:
                res.append(current.copy())
                return

            if i >= len(candidates) or total > target:
                return

            for j in range(i, len(candidates)):
                if  j > i and candidates[j] == candidates[j-1]:
                    continue
                # include
                current.append(candidates[j])
                backtrack(j+1, current, total+candidates[j])

                current.pop()
                # exclude
                


        # call backtrack
        backtrack(0, [], 0)
        # return result
        return res
