class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodAll = 1
        ans = []
        zeros = 0
        for value in nums:
            if value == 0:
                zeros += 1
                continue
            prodAll = prodAll * value
        
        if zeros > 1:
            prodAll = 0
            return [0]*len(nums)

        if 0 in nums:
            for value in nums:
                if value == 0:
                    ans.append(prodAll)
                else:
                    ans.append(0)
            return ans;
        
        for value in nums:
            print(prodAll,value)    
            ans.append(prodAll // value)
        
        return ans