"""
https://leetcode-cn.com/problems/pascals-triangle
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rst = [
            [1] * ith
            for ith in range(1, numRows+1)
        ]
        for i in range(1, numRows):
            for j in range(1, len(rst[i])-1):
                rst[i][j] = rst[i-1][j] + rst[i-1][j-1]
        return rst


for line in Solution().generate(11):
    print(line)
