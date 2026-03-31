class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures)):
            right = i + 1
            while right < len(temperatures):
                if temperatures[right] > temperatures[i]:
                    ans.append(len(temperatures[i:right]))
                    break
                right += 1
            if right == len(temperatures):
                ans.append(0)
        return ans

            
