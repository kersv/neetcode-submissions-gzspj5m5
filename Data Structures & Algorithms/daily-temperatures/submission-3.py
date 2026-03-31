class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # TC = O(n^2) SC = O(1)
        # ans = []
        # for i in range(len(temperatures)):
        #     right = i + 1
        #     while right < len(temperatures):
        #         if temperatures[right] > temperatures[i]:
        #             ans.append(right - i)
        #             break
        #         right += 1
        #     if right == len(temperatures):
        #         ans.append(0)
        # return ans

        # TC = O(n) SC = O(n)
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([temp,i])
        return res


            
