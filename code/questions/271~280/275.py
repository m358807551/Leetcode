"""
https://leetcode-cn.com/problems/h-index-ii
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right = 0, len(citations)-1
        while left < right:
            mid = left + (right-left) // 2
            if citations[mid] < len(citations)-mid:
                left = mid+1
            else:
                right = mid
        if citations[left] >= len(citations)-left:
            return len(citations)-left
        else:
            return 0


print(
    Solution().hIndex(
        [0, 0, 0, 1, 2]
    )
)
