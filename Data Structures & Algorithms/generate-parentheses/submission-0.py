class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # res 
        res = []

        # backtrack
        def backtrack(current, openCount, closeCount):
            # base case
            if n*2 == len(current):
                res.append(current)
                return

            # include
            if openCount < n:
                backtrack(current + "(", openCount+1, closeCount)

            # exclude
            if closeCount < openCount:
                backtrack(current + ")", openCount, closeCount+1)

        backtrack("", 0, 0)
        return res