"""
https://leetcode-cn.com/problems/jump-game-ii/
"""


class Solution:
    def jump(self, nums):
        rst = left = right = 0
        while right < len(nums)-1:
            max_ = 0
            for i in range(left, right+1):
                max_ = max(max_, i + nums[i])
            left = right + 1
            right = max_
            rst += 1
        return rst


print(
    Solution().jump(
        [2, 3, 1, 1, 4]
    )
)
