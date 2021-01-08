"""
https://leetcode-cn.com/problems/unique-paths-ii
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        matrix = obstacleGrid
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])

        dp = [
            [0] * n
            for _ in range(m)
        ]
        for j in range(n):
            if matrix[0][j]:
                break
            else:
                dp[0][j] = 1

        for i in range(m):
            if matrix[i][0]:
                break
            else:
                dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if matrix[i-1][j] == 0:
                    dp[i][j] += dp[i-1][j]
                if matrix[i][j-1] == 0:
                    dp[i][j] += dp[i][j-1]

        return dp[-1][-1]


print(
    Solution().uniquePathsWithObstacles(
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
    )
)
