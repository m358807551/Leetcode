"""
https://leetcode-cn.com/problems/triangle
"""
from functools import lru_cache


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.matrix = triangle
        return self.res(0, 0)

    @lru_cache(None)
    def res(self, i, j):
        if i == len(self.matrix)-1:
            return self.matrix[i][j]
        elif i > len(self.matrix)-1:
            return 0
        return self.matrix[i][j] + min(self.res(i+1, j), self.res(i+1, j+1))

t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(
    Solution().minimumTotal(t)
)
