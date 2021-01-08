"""
https://leetcode-cn.com/problems/meeting-rooms-ii/
"""


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        arr = []
        for interval in intervals:
            arr.append((interval[0], 1))
            arr.append((interval[1], -1))
        arr.sort()
        rst = now = 0
        for _, t in arr:
            now += t
            rst = max(rst, now)
        return rst


print(
    Solution().minMeetingRooms(
[[7,10],[2,4]]
    )
)
