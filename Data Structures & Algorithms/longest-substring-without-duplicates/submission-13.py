class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        uniqueString = set()
        left, right = 0, 0
        longString = 0

        if len(s) <= 1:
            return len(s)
        
        "zxyzxyz"
        while right < len(s):
            while s[right] in uniqueString:
                uniqueString.remove(s[left])
                left+=1
            uniqueString.add(s[right])
            longString = max(longString, right-left+1)
            right+=1

        return longString
        'z'
        'z,x'
        'z,x,y'
        'z,x,y,z'
        'x,y,z,x'
        'y,z,x,y'
        'z,x,y,z'
        'x,y,z' 

