class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        mapS = {}
        mapT = {}

        for i,j in zip(s,t):
            mapS[i] = mapS.get(i,0)+1
            mapT[j] = mapT.get(j,0)+1
        
        return mapS == mapT

        

        