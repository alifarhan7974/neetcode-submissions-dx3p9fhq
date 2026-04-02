class Solution:
    def climbStairs(self, n: int) -> int:
        # index = num of starirs to climb
        stairs = [0, 1, 2]

        for i in range(3, n+1): 
            stairs.append(stairs[-1] + stairs[-2])
            #stairs.pop(0)


        return stairs[n]