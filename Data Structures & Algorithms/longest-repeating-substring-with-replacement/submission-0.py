class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # COME BACK TO THIS PLS
        countMap = {}
        lengthRes = 0

        left = 0
        for right in range(len(s)):
            countMap[s[right]] = countMap.get(s[right], 0) + 1

            if (right - left + 1) - max(countMap.values()) > k:
                countMap[s[left]] -= 1
                left += 1

            lengthRes = max(lengthRes, right - left + 1)
        return lengthRes
            

        

