"""
https://leetcode-cn.com/problems/strobogrammatic-number-ii/
"""


class Helper(object):

    def __init__(self, number_n):
        if number_n % 2 == 0:
            n = number_n // 2
        else:
            n = (number_n+1) // 2
        self.arr = [0] * n
        self.is_three = True if number_n % 2 else False
        if not(self.is_three and n ==1):
            self.arr[0] = 1

    def inc(self):
        return self.inc_i(len(self.arr)-1)

    def inc_i(self, i):
        if i < 0:
            if not self.is_three:
                self.arr.insert(0, 1)
            self.is_three = not self.is_three
            return True
        self.arr[i] += 1
        if (self.arr[i] == 5) or (self.is_three and self.arr[-1] == 3):
            self.arr[i] = 0
            return self.inc_i(i-1)

    def show(self):
        if self.is_three:
            mid = '018'[self.arr[-1]]
            left = ''.join(['01689'[x] for x in self.arr[:-1]])
        else:
            mid = ''
            left = ''.join(['01689'[x] for x in self.arr])
        right = left[::-1].replace('6', '*').replace('9', '6').replace('*', '9')
        return left + mid + right


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        helper = Helper(n)
        rst = []
        while True:
            rst.append(helper.show())
            if helper.inc():
                break
        return rst

print(
    Solution().findStrobogrammatic(2)
)
