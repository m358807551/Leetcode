"""
https://leetcode-cn.com/problems/count-and-say/
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        rst = '1'
        for _ in range(n-1):
            stack = []
            new = ''
            for letter in rst:
                if stack and stack[-1] != letter:
                    new += str(len(stack)) + stack[0]
                    stack = []
                stack.append(letter)
            new += str(len(stack)) + stack[0]
            rst = new
        return rst


print(
    Solution().countAndSay(
        5
    )
)
