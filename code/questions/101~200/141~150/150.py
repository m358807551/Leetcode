"""
https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in "+-*/":
                num2, num1 = stack.pop(-1), stack.pop(-1)
                rst = eval(str(num1) + token + str(num2))
                stack.append(int(rst))
            else:
                stack.append(int(token))
        return stack[0]


print(
    Solution().evalRPN(
        # ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)

"""
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
