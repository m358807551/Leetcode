"""
https://leetcode-cn.com/problems/paint-house/
"""


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        dp = [[0, 0, 0] for _ in range(len(costs))]
        dp[0][:] = costs[0]
        for i in range(1, len(costs)):
            dp[i][0] = costs[i][0] + min(
                 dp[i-1][1],
                 dp[i-1][2],
            )

            dp[i][1] = costs[i][1] + min(
                dp[i - 1][0],
                dp[i - 1][2],
            )

            dp[i][2] = costs[i][2] + min(
                dp[i - 1][0],
                dp[i - 1][1],
            )
        return min(dp[len(costs)-1])


print(
    Solution().minCost(
[
    [6,4,13],
    [10,9,15]]
    )
)
