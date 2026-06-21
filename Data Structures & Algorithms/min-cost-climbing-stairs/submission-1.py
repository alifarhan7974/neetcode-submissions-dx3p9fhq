class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Base case 
        if len(cost) == 1: 
            return 0

        if len(cost) == 2: 
            return min(cost)

        # Dp is cost to reach that index, so no cost to start? 
        dp = [0] * len(cost)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost)): 
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])

        print(dp) 
        return min(dp[-1] + cost[-1], dp[-2] + cost[-2])




