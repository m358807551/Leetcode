"""
https://leetcode-cn.com/problems/valid-number
"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except:
            return False


a = Solution().isNumber(' 6e-1')
print(a)
