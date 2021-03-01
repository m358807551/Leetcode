"""
https://leetcode-cn.com/problems/longest-valid-parentheses/
"""
from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        queue = deque()
        rst = 0
        s += '!'
        for i, letter in enumerate(s):
            if letter == '(':
                queue.append([len(queue), 0])
            else:
                if letter == ')' and queue and queue[-1][1] == 0:
                    queue.appendleft(queue.pop())
                    queue[0][1] = 1
                else:
                    d = dict(queue)
                    max_ = 0
                    for j in range(len(d)):
                        if d[j]:
                            max_ += 1
                            rst = max(rst, max_)
                        else:
                            max_ = 0

                    queue = deque()
        return rst * 2


print(
    Solution().longestValidParentheses(
        '(()()',  # 4
        # ')()())',  # 4
        # '()(()',  # 2
        # '(()))())(',  # 4
        # ')()())',  # 4
    )
)
