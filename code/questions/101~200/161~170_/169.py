"""
https://leetcode-cn.com/problems/majority-element
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        type_, n = None, 0
        for num in nums:
            if type_ is None:
                type_ = num
                n += 1
            elif num == type_:
                n += 1
            else:
                n -= 1
                if n < 1:
                    type_ = None
        return type_


print(
    Solution().majorityElement(
[2,2,1,1,1,2,2]
    )
)
