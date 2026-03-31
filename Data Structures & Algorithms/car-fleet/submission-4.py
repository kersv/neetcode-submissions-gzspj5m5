class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # create arr to store the speed to reach target. [position, speed]
        sortPos = []
        for pos,spd in zip(position, speed):
            sortPos.append([pos,spd])
        

        # sort arr in descending order by position
        sortPos.sort(reverse=True)

        # create a stack 
        stack = []
        # loop through array
        for car in sortPos:
            print(car[0], car[1])
            steps = (target - car[0]) / car[1]
            print(steps)
            # append to stack the steps if stack is empty
            if not stack:
                stack.append(steps)
            # check if next step is mores steps compare to stack[-1]
            # append the current step
            elif stack and stack[-1] < steps:
                stack.append(steps)

        print(stack)
        # return the len(stack)
        return len(stack)

