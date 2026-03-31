class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        hashmapAnagram = {}
        for value in strs:
            key = tuple(sorted(value))
            if key in hashmapAnagram:
                hashmapAnagram[key].append(value)
            else:
                hashmapAnagram[key] = [value]

        return list(hashmapAnagram.values())


            