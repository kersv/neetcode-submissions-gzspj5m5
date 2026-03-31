class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        # Start: left = 0, right = 0.
        left, right = 0, 0
        # Grow: right moves, you add to HASHMAP.
        freqMap = {}
        maxFreq = 0
        maxLength = 0
        while right < len(s):

            freqMap[s[right]] = freqMap.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freqMap[s[right]])
            # Check: Is the window "broken"?
            while (right - left+1) - maxFreq > k:
                # Shrink: If broken, move left and update HASHMAP.
                freqMap[s[left]] = freqMap[s[left]]-1
                left+=1
            # Record: Always keep track of the biggest "legal" window size you've seen.
            maxLength = max(maxLength, (right - left)+1)
            right+=1
        
        return maxLength