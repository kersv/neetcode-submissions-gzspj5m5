class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TC = O(n) SC = O(n)
        valueSet = set()
        longestSubstring = 0

        left = 0
        right = left
        while right < len(s):
            if s[right] not in valueSet:
                valueSet.add(s[right])
                longestSubstring = max(longestSubstring, len(valueSet))
                right += 1
            else: 
                valueSet.remove(s[left])
                left += 1
        return longestSubstring

    

