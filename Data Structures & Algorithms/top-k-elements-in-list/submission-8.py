class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {value : frequency} hashmap
        hashFreq = {}

        for value in nums:
            if value in hashFreq:
                hashFreq[value] += 1
            else:
                hashFreq[value] = 1
        
        ans = []
        pairs = list(hashFreq.items())
        freqPairs = sorted(pairs, key=lambda x:x[1], reverse=True)
        print(freqPairs)
        for i in range(0, k):
            ans.append(freqPairs[i][0])

        return ans



            