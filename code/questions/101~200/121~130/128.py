"""
https://leetcode-cn.com/problems/longest-consecutive-sequence
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        nums = set(nums)
        for num in nums:
            if num-1 in nums:
                continue
            cur = num
            while cur in nums:
                cur += 1
            rst = max(rst, cur-num)
        return rst


print(
    Solution().longestConsecutive([100, 4, 200, 1, 3, 2]),
)
