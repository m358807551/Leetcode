"""
https://leetcode-cn.com/problems/dungeon-game
"""
from functools import lru_cache


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        nrows, ncols = len(dungeon), len(dungeon[0])
        dp = [
            [float("inf")] * (ncols+1)
            for _ in range(nrows+1)
        ]
        for r in range(nrows-1, -1, -1):
            for c in range(ncols-1, -1, -1):
                if r == nrows-1 and c == ncols - 1:
                    dp[r][c] = max(1-dungeon[r][c], 1)
                else:
                    dp[r][c] = min(
                        max(dp[r][c + 1] - dungeon[r][c], 1),
                        max(dp[r + 1][c] - dungeon[r][c], 1)
                    )

        return dp[0][0]

print(
    Solution().calculateMinimumHP(
[[-2,-3,3],[-5,-10,1],[10,30,-5]]
    )
)
