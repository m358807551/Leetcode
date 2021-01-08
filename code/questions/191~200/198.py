"""
https://leetcode-cn.com/problems/house-robber
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * (len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, len(dp)):
            dp[k] = max(
                nums[k-1] + dp[k-2],
                dp[k-1]
            )
        return dp[-1]


print(
    Solution().rob(
[1, 2, 3, 1]
    )
)
