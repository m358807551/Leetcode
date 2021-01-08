"""
https://leetcode-cn.com/problems/divide-two-integers/
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = True if dividend < 0 < divisor or divisor < 0 < dividend else False
        dividend, divisor = abs(dividend), abs(divisor)
        a, b = [1], [divisor]
        while b[-1] <= dividend:
            a.append(a[-1]+a[-1])
            b.append(b[-1]+b[-1])
        rst = 0
        for j in range(len(a)-2, -1, -1):
            if dividend >= b[j]:
                dividend -= b[j]
                rst += a[j]
        rst = -rst if neg else rst
        return rst if  -2**31<= rst <= 2**31-1 else 2**31-1


print(
    Solution().divide(
        10, -2
    )
)
