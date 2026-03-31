class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # palindrome is true if the string is the same read backwards
        # skip if not a char
        left = 0
        right = len(s)-1
        while left < right:
            # check if s[left] is char, move left if not
            if not s[left].isalnum():
                left+=1
                continue
            # check if s[right] is char, move left if not
            if not s[right].isalnum():
                right-=1
                continue
            # check if left and right equal
            if s[left].lower() != s[right].lower():
                print(s[left].lower(), s[right].lower())
                return False
            else:
                left+=1
                right-=1
        return True