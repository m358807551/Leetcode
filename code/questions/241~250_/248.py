"""
https://leetcode-cn.com/problems/strobogrammatic-number-iii/
"""


class TargetNumber(object):
    def __init__(self):
        self.is_ternary = True  # 个位是三进制？
        self.arr = [0]

    def inc(self):
        self.inc_i(len(self.arr)-1)

    def inc_i(self, i):
        if i == -1:
            if not self.is_ternary:
                self.arr = [1] + self.arr
            self.arr[0] = 1
            self.is_ternary = not self.is_ternary
            return
        self.arr[i] += 1
        if (
            (i == len(self.arr) - 1)
            and self.is_ternary
            and self.arr[i] == 3
        ) or (
            self.arr[i] == 5
        ):
            self.arr[i] = 0
            self.inc_i(i-1)

    def show(self):
        rst = {0: '0', 1: '1', 2: '8'}[self.arr[-1]] if self.is_ternary else ''
        start = len(self.arr)-2 if self.is_ternary else len(self.arr) - 1
        for j in range(start, -1, -1):
            if self.arr[j] == 2:
                rst = '6' + rst + '9'
            elif self.arr[j] == 4:
                rst = '9' + rst + '6'
            elif self.arr[j] == 3:
                rst = '8' + rst + '8'
            else:
                rst = str(self.arr[j]) + rst + str(self.arr[j])
        return rst


class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        rst = 0
        number = TargetNumber()
        value = number.show()
        while int(value) <= int(high):
            if int(value) >= int(low):
                rst += 1
            number.inc()
            value = number.show()
        return rst


print(
    Solution().strobogrammaticInRange('50', '100')
)
