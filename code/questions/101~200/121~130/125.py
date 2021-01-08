"""
https://leetcode-cn.com/problems/valid-palindrome/
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.upper()
        s = [letter for letter in s if s.isalnum()]
        return s == s[::-1]


print(
    Solution().isPalindrome("A man, a plan, a canal: Panama")
)
