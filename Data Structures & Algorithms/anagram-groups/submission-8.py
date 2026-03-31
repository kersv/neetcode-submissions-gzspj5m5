class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortMap = {}

        for string in strs:
            sortedStr = "".join(sorted(string))
            if sortedStr not in sortMap:
                sortMap[sortedStr] = []
            sortMap[sortedStr].append(string)

        
        return list(sortMap.values())



        