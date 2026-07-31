class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       
       i,j = 0, len(numbers)-1

       while i <= j:
        print(i, j)
        sumTarget = numbers[i] + numbers[j]
        if target == sumTarget:
            return [i+1, j+1]
        elif sumTarget > target:
            j-=1
        else:
            i+=1
        



        