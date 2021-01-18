"""
https://leetcode-cn.com/problems/fraction-to-recurring-decimal
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, d = int(numerator), int(denominator)
        rst1 = n // d
        y = n % d
        rst2 = []
        while (y*10) // d not in rst2:
            rst2.append( y*10 // d)
            y = y*10 % d

        if y:
            rst2.insert(rst2.index((y*10) // d), '(')
            rst2.append(')')
        rst2 = ''.join(
            [str(x) for x in rst2]
        )
        rst2 = rst2.rstrip('0')
        if rst2:
            rst2 = '.' + rst2

        flag = -1 if numerator * denominator < 0 else 1
        if flag == -1:
            return '-{}{}'.format(rst1, rst2)
        return '{}{}'.format(rst1, rst2)


print(
    Solution().fractionToDecimal(1, 333)
)
