class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # # TC = O(nlogn) SC = O(1)
        # sortS = ''.join(sorted(s))
        # sortT = ''.join(sorted(t))
        
        # return sortS == sortT

        # TC = O(n) SC = O(n) 
        if len(s) != len(t):
            return False
        
        mapS = {}
        mapT = {}

        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i], 0) + 1
            mapT[t[i]] = mapT.get(t[i], 0) + 1
        
        return mapS == mapT
