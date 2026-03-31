class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {value : frequency} hashmap
        hashFreq = {}

        buckets = [[] for i in range(len(nums)+1)]
        ans = []
        for num in nums:
            if num in hashFreq:
                hashFreq[num] += 1
            else:
                hashFreq[num] = 1
        
        for key,value in hashFreq.items():
            buckets[value].append(key)

        print(buckets)
        print(hashFreq.items())
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans



            