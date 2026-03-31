class Solution:
    def isValid(self, s: str) -> bool:
        # TC = O(n) SC = O(n)
        stack = []
        map = { ']':'[', ')':'(', '}':'{' }

        for char in s:
            if char in map:
                if len(stack) != 0 and stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

                
        return len(stack) == 0
