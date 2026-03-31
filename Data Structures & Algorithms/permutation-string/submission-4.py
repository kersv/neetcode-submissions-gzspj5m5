class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # use a hashmap to store s1 and s2 to compare to
        s1Map = {}
        s2Map = {}
        for char in s1:
            s1Map[char] = s1Map.get(char, 0) +1
        # s2, left and right pointers. start 0,0
        left, right = 0, 0
        # while right < len(s2)
        while right < len(s2):
            # check if m
            s2Map[s2[right]] = s2Map.get(s2[right],0) +1
            print(s2Map)
            if s1Map == s2Map:
                return True
            elif right - left + 1 > len(s1)-1:
                s2Map[s2[left]]-=1
                if s2Map[s2[left]] == 0:
                    del s2Map[s2[left]]
                left+=1
            right+=1
            # check if current window matches s1 hashmap, return true
        # if it doesnt pass while loop
        print(s2Map)
        return False