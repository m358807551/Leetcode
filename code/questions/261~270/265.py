"""
https://leetcode-cn.com/problems/paint-house-ii/
"""


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        k = len(costs[0])
        dp = [[0] * k for _ in range(len(costs))]
        dp[0][:] = costs[0]
        for i in range(1, len(costs)):
            for j in range(k):
                dp[i][j] = costs[i][j] + min(dp[i-1][m] for m in range(k) if m != j)
        return min(dp[len(costs)-1])

print(
    Solution().minCostII(
[[1,5,3],[2,9,4]]
    )
)
