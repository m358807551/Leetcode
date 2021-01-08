"""
https://leetcode-cn.com/problems/house-robber-ii
"""

from functools import lru_cache


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp1 = [0] * (len(nums)+2)
        dp2 = dp1[:]
        for i in range(len(nums)-1):
            dp1[i] = max(
                nums[i] + dp1[i-2],
                dp1[i-1]
            )

        for i in range(1, len(nums)):
            dp2[i] = max(
                nums[i] + dp2[i-2],
                dp2[i-1]
            )

        return max(dp1[len(nums)-2], dp2[len(nums)-1])


print(
    Solution().rob(
[1]

    )
)
