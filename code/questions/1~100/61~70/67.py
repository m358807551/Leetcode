"""
https://leetcode-cn.com/problems/add-binary
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j, f = len(a)-1, len(b)-1, 0
        rst = ''
        while i >= 0 or j >= 0 or f:
            v = f
            if i >= 0:
                v += int(a[i])
                i -= 1
            if j >= 0:
                v += int(b[j])
                j -= 1
            f = v // 2
            v = v % 2
            rst = str(v) + rst
        return rst


a = '1111010'
b = '1011'

print(Solution().addBinary(a, b))
