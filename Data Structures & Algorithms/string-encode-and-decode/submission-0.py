class Solution:

    def encode(self, strs: List[str]) -> str:
        # return ans string
        ans = ""
        # for each string in strings
        for s in strs:
            # append the lengh of the string with '#' followed by the string itself
            ans += str(len(s)) + '#' + s
        # return the ans
        return ans

    def decode(self, s: str) -> List[str]:
        #4#neet4#code4#love3#you
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i = j+1+length
        return ans

