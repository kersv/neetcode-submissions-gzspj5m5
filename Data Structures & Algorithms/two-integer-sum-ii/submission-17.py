class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}

        for idx, num in enumerate(numbers):
            comp = target - num
            if comp in hmap:
                return [hmap[comp], idx+1]
            hmap[num] = idx + 1



        