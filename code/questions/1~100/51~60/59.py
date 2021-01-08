"""
https://leetcode-cn.com/problems/spiral-matrix-ii
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [
            [0] * n
            for _ in range(n)
        ]
        x = 1
        up, down, left, right = 0, n-1, 0, n-1
        while True:
            for j in range(left, right+1):
                matrix[up][j] = x
                x += 1
            up += 1
            if not (up <= down and left <= right):
                break

            for i in range(up, down+1):
                matrix[i][right] = x
                x += 1
            right -= 1
            if not (up <= down and left <= right):
                break

            for j in range(right, left-1, -1):
                matrix[down][j] = x
                x += 1
            down -= 1
            if not (up <= down and left <= right):
                break

            for i in range(down, up-1, -1):
                matrix[i][left] = x
                x += 1
            left += 1
            if not (up <= down and left <= right):
                break

        return matrix


print(
    Solution().generateMatrix(3)
)
