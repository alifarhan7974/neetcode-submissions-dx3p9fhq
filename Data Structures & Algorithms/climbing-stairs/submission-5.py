class Solution:
    def climbStairs(self, n: int) -> int:
        # index = num of starirs to climb
        stairs = [0, 1, 2]
        if n <= 2: 
            return stairs[n]

        for i in range(3, n+1): 
            stairs.append(stairs[-1] + stairs[-2])
            stairs.pop(0)

        #print(stairs)
        return stairs[-1]