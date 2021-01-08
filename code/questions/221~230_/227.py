"""
https://leetcode-cn.com/problems/basic-calculator-ii
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        s = re.sub('[^0-9]', lambda x: '!{}!'.format(x.group()), s)
        s = [x for x in s.split('!') if x.strip()]
        queue, stack = [], []
        levels = {'+': 1, '-': 1, '*': 10, '/': 10}
        for x in s:
            if x in '+-*/':
                while stack and levels[stack[-1]] >= levels[x]:
                    queue.append(stack.pop(-1))
                stack.append(x)
            else:
                queue.append(int(x))
        while stack:
            queue.append(stack.pop(-1))

        for x in queue:
            if isinstance(x, int):
                stack.append(x)
            else:
                stack.append({
                        '+': lambda a, b: a+b,
                        '-': lambda a, b: a-b,
                        '*': lambda a, b: a*b,
                        '/': lambda a, b: a//b,
                    }[x](stack.pop(-2), stack.pop(-1))
                )
        return stack[0]

print(
    Solution().calculate(
        '1 + 2 * 3'
    )
)
