class Solution:
    def isValid(self, s: str) -> bool:
        # { : } , [ : ], ( : ) matches
        stack = []

        hMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{" 
        }

        if len(s) <= 1:
            return False

        for char in s:
            if char in hMap.values():
                stack.append(char)
            else:
                if len(stack) <= 0:
                    return False
                top_element = stack.pop()
                if hMap[char] != top_element:
                    return False
        if len(stack) > 0:
            return False
        return True


        