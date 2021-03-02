"""
https://leetcode-cn.com/problems/plus-one
"""


class Solution:
    def plusOne(self, digits):
        i, j = len(digits)-1, True
        while i >= 0 and j:
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] %= 10
            else:
                j = False
            i -= 1
        if j:
            digits = [1] + digits
        return digits


print(
    Solution().plusOne([1, 2, 9])
)
