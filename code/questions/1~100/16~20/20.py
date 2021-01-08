"""
https://leetcode-cn.com/problems/valid-parentheses/
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {')': '(', ']': '[', '}': '{'}
        stack = []
        for letter in s:
            if letter in d.values():
                stack.append(letter)
            elif stack and d[letter] == stack[-1]:
                stack.pop(-1)
            else:
                return False
        return not stack


print(
    Solution().isValid(
 "()"
    )
)
