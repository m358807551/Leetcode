"""
https://leetcode-cn.com/problems/minimum-size-subarray-sum
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = right = 0
        count = 0
        rst = float('inf')
        for right in range(len(nums)):
            count += nums[right]
            for left in range(left, right+1):
                if count >= s:
                    rst = min(rst, right-left+1)
                else:
                    break
                count -= nums[left]

        return rst if rst != float('inf') else 0


print(
    Solution().minSubArrayLen(
        7,
        [2, 3, 1, 2, 4, 3]
    )
)
