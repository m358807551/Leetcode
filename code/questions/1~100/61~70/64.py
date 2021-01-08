"""
https://leetcode-cn.com/problems/minimum-path-sum
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [
            [0] * n
            for _ in range(m)
        ]

        dp[0][0] = grid[0][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]


print(
    Solution().minPathSum(
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    )
)
