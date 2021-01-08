"""
https://leetcode-cn.com/problems/h-index
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        if not citations or not citations[-1]:
            return 0
        left, right = 0, len(citations) - 1
        while left < right:
            mid = left + (right-left)//2
            if citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                right = mid
        return len(citations) - left

print(
    Solution().hIndex(
        [1, 0]
    )
)
