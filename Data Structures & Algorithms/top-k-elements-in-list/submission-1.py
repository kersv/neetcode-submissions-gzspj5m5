class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashmap for each number to store count
        count = {}
        # create an array of length of nums to hold empty array
        freq = [[] for i in range(len(nums)+1)] 

        # set count for each num in nums
        for num in nums:
            count[num] = 1 + count.get(num, 0) 
        # for each count add value to the array at counter index
        for n, c in count.items():
            freq[c].append(n)

        # return ans array
        ans = []
        # loop in reverse of freq
        for i in range(len(freq)-1, 0, -1):
            # for number in freq append to ans 
            for n in freq[i]:
                ans.append(n)

                # if length of ans is equal to k return ans
                if len(ans) == k:
                    return ans
                
                

        