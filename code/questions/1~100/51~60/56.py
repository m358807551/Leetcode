"""
https://leetcode-cn.com/problems/merge-intervals
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        rtn = []
        for x in intervals:
            if not rtn:
                rtn.append(x)
                continue
            if x[0] > rtn[-1][1]:
                rtn.append(x)
            else:
                rtn[-1][1] = max(rtn[-1][1], x[1])
        return rtn


s = [[1,3],[2,6],[8,10],[15,18]]
print(
    Solution().merge(s)
)
