"""
https://leetcode-cn.com/problems/spiral-matrix/
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        rst = []
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m-1, 0, n-1
        while True:
            for j in range(left, right+1):
                rst.append(matrix[up][j])
            up += 1
            if up > down:
                break

            for i in range(up, down+1):
                rst.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for j in range(right, left-1, -1):
                rst.append(matrix[down][j])
            down -= 1
            if up > down:
                break

            for i in range(down, up-1, -1):
                rst.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return rst


s = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution().spiralOrder(s))
