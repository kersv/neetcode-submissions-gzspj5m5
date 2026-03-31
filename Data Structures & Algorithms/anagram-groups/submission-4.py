class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # TC = O(nlogn) SC = O(n)
        map = {}

        for word in strs:
            sortStr = ''.join(sorted(word))
            if sortStr not in map:
                map[sortStr] = []
            
            map[sortStr].append(word)
        
        return map.values()

        