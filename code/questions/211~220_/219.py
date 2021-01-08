"""
https://leetcode-cn.com/problems/contains-duplicate-ii
"""
from collections import defaultdict


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            if dic[num]:
                if i - dic[num][-1] <= k:
                    return True
            dic[num].append(i)
        return False

print(
    Solution().containsNearbyDuplicate(
        [1, 2, 3, 1, 2, 3],
        3
    )
)
