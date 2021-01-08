"""
https://leetcode-cn.com/problems/insert-interval
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # 先找到插入位置
        if not intervals:
            return [newInterval]

        if intervals[-1][0] < newInterval[0]:
            if intervals[-1][1] < newInterval[0]:
                return intervals + [newInterval]
            else:
                intervals[-1][1] = max(intervals[-1][1], newInterval[1])
                return intervals

        left, right = 0, len(intervals)-1
        while left < right:
            mid = left + (right-left) // 2
            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            else:
                right = mid

        rst = intervals[: left]
        # rst.append(newInterval)
        if (not rst) or rst[-1][1] < newInterval[0]:
            rst.append(newInterval)
        else:
            rst[-1][1] = max(rst[-1][1], newInterval[1])

        for i in range(left, len(intervals)):
            if rst[-1][1] < intervals[i][0]:
                rst.append(intervals[i])
            else:
                rst[-1][1] = max(rst[-1][1], intervals[i][1])
        return rst


intervals = [[1, 5]]
newInterval = [1, 7]
print(
    Solution().insert(intervals, newInterval)
)
