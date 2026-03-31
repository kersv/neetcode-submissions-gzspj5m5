class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longSeq = 0
        currSeq = 1
        # convert list to hashset, to remove duplicates and for faster lookup
        numSet = set(nums)
        print(numSet, len(numSet))
        for val in numSet:
            if val -1 not in numSet:
                currSeq = 1
                while (val + currSeq) in numSet:
                    currSeq += 1
            longSeq = max(longSeq, currSeq)
            
        return longSeq
