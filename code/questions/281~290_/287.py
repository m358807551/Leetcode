"""
https://leetcode-cn.com/problems/find-the-duplicate-number/
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        t = 0
        while t != slow:
            t = nums[t]
            slow = nums[slow]
        return t


print(
    Solution().findDuplicate(
        [1, 2, 2, 3]
    )
)
