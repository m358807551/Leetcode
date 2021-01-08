"""
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        rst = ['']
        for digit in digits:
            rst = [x+letter for x in rst for letter in d[digit]]
        return rst


print(
    Solution().letterCombinations(
        '23'
    )
)
