from collections import deque 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = [] # least time to most time  

        for p, s in cars: 
            time = (target - p) / s 

            # curr car reaches top of stack car
            if stack and time <= stack[-1]: 
                continue
            # curr car does not reach top of stack car 
            else: 
                stack.append(time)

        return len(stack) 

            

        

    