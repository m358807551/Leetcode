"""
https://leetcode-cn.com/problems/set-matrix-zeroes
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        for j in cols:
            for i in range(m):
                matrix[i][j] = 0


s = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Solution().setZeroes(s)

print(s)
