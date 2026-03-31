class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operator = ['+', '-', '*', '/']
        
        stack = []

        for char in tokens:
            if char not in operator:
                stack.append(int(char))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if char == '+':
                    twoSum = int(num1 + num2)

                    stack.append(twoSum)
                elif char == '-':
                    twoSub = int(num2 - num1)
                    stack.append(twoSub)
                elif char == '*':
                    twoProd = int(num1 * num2)
                    stack.append(twoProd)
                else:
                    twoDiv = int(num2 / num1)
                    stack.append(twoDiv)

        return stack.pop()
            