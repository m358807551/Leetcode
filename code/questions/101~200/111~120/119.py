"""
https://leetcode-cn.com/problems/pascals-triangle-ii
"""


class Solution(object):
    def getRow(self, rowIndex):
        rst = [1] * (rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                rst[j] += rst[j-1]
        return rst


print(
    Solution().getRow(3)
)
