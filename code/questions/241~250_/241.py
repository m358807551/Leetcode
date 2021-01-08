"""
https://leetcode-cn.com/problems/different-ways-to-add-parentheses/
"""


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        rst = []
        for i, letter in enumerate(input):
            if letter not in '+-*':
                continue
            left = self.diffWaysToCompute(input[:i])
            right = self.diffWaysToCompute(input[i+1:])
            for x in left:
                for y in right:
                    rst.append({
                        '+': lambda a, b: a+b,
                        '-': lambda a, b: a-b,
                        '*': lambda a, b: a*b,
                    }[letter](x, y))
        return rst


print(
    Solution().diffWaysToCompute(
        '2*3-4*5'
    )
)
