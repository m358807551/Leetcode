"""
https://leetcode-cn.com/problems/maximum-subarray
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = float('-inf')
        t = 0
        for num in nums:
            t += num
            rst = max(rst, t)
            if t < 0:
                t = 0
        return rst


s = [-2,1,-3,4,-1,2,1,-5,4]

print(
    Solution().maxSubArray(s)
)
