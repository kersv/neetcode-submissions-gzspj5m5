class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # return ans with default 0 placeholders
        ans = [0] * len(temperatures)
        # initialize stack
        stack = []
        # for loop for every index with value utilizing enumerate
        for i, val in enumerate(temperatures):
            # while loop currTemp > stack's recent Temp and stack has value:
            while stack and val > stack[-1][1]:
                # pop from stack and save the difference in days to ans at index
                prevTemp = stack.pop()
                ans[prevTemp[0]] = i - prevTemp[0] 

            # append current temp to stack outside while loop
            stack.append([i,val])


        # return stack outide for loop
        return ans