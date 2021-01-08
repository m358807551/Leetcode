"""
https://leetcode-cn.com/problems/contains-duplicate-iii
"""
from collections import defaultdict


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or k < 0:
            return False
        buckets = defaultdict(list)
        for i, num in enumerate(nums):
            i_bucket = num // (t+1)
            if buckets[i_bucket]:
                return True
            if buckets[i_bucket-1] and (abs(buckets[i_bucket-1][0] - num) <= t):
                return True
            if buckets[i_bucket+1] and (abs(buckets[i_bucket+1][0] - num) <= t):
                return True
            buckets[i_bucket].append(num)
            if i >= k:
                buckets[nums[i-k] // (t+1)] = []

        return False


print(
    Solution().containsNearbyAlmostDuplicate(
        nums=[1, 0, 1, 1], k=1, t=2
    )
)
