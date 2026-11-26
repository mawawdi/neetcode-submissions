class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one_step, two_steps = cost[n - 2], cost[n - 1]
        for i in range(n - 3, -1, -1):
            one_step, two_steps = cost[i] + min(one_step, two_steps), one_step

        return min(one_step, two_steps)