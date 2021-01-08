"""
https://leetcode-cn.com/problems/basic-calculator
"""
import re


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = re.sub('[^0-9]', lambda x: '!{}!'.format(x.group()), s)
        s = [x for x in s.split('!') if x.strip()]
        queue, stack = [], []
        for x in s:
            if x == '(':
                stack.append(x)
            elif x in '+-':
                while stack and stack[-1] in '+-':
                    queue.append(stack.pop(-1))
                stack.append(x)
            elif x == ')':
                while stack[-1] != '(':
                    queue.append(stack.pop(-1))
                stack.pop(-1)
            else:
                queue.append(int(x))
        while stack:
            queue.append(stack.pop(-1))

        stack = []
        for x in queue:
            if x == '+':
                stack.append(stack.pop(-2) + stack.pop(-1))
            elif x == '-':
                stack.append(stack.pop(-2) - stack.pop(-1))
            else:
                stack.append(x)
        return stack[0]


print(
Solution().calculate(
'(71)-(0)+(14)'
)
)
