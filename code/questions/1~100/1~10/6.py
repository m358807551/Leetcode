"""
https://leetcode-cn.com/problems/zigzag-conversion/
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        matrix = [[] for _ in range(numRows)]
        inc = 1
        left, right = 0, numRows-1
        i = 0
        for letter in s:
            matrix[i].append(letter)
            i += inc
            if i in {left, right}:
                inc = -inc

        return ''.join(''.join(arr) for arr in matrix)


print(
    Solution().convert(
        "PAYPALISHIRING",
        3
    )
)
