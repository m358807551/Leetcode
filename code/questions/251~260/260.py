"""
https://leetcode-cn.com/problems/single-number-iii/
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = 0
        for num in nums:
            a ^= num
        b = c = 0
        for num in nums:
            if (num >> (len(bin(a)) - 3)) & 1:
                b ^= num
            else:
                c ^= num
        return [b, c]

print(
    Solution().singleNumber(
[1,2,1,3,2,5]
    )
)
