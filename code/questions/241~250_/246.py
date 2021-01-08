"""
https://leetcode-cn.com/problems/strobogrammatic-number/
"""


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        left, right = 0, len(num)-1
        while left < right:
            if num[left]+num[right] not in '00 11 88 69 96'.split():
                return False
            left += 1
            right -= 1
        return num[left] in '018' if left == right else True


print(

)
