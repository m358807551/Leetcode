"""
https://leetcode-cn.com/problems/multiply-strings/
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = [int(letter) for letter in num1[::-1]]
        num2 = [int(letter) for letter in num2[::-1]]
        rst = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                x = num1[i]*num2[j]
                rst[i+j] += x % 10
                rst[i+j+1] += x // 10

        for i in range(len(rst)-1):
            rst[i+1] += rst[i] // 10
            rst[i] = rst[i] % 10

        return ''.join([str(x) for x in rst[::-1]]).lstrip('0') or '0'

print(
    Solution().multiply(
        '123',
        '45'
    )
)
