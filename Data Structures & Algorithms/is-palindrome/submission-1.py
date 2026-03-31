class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''
        for char in s:
            if (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9')):
                newString += char.lower()
        
        left = 0
        right = len(newString)-1
        while left < right:
            if newString[left] != newString[right]:
                return False
            left += 1
            right -= 1
        return True

        
            