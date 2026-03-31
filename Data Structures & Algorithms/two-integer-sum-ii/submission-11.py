class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hashNum = {}

        for i, num in enumerate(numbers):
            comp = target - num
            if comp in hashNum:
                return [hashNum[comp]+1,i+1]
            hashNum[num] = i

        return []
        