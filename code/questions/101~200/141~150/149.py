"""
https://leetcode-cn.com/problems/max-points-on-a-line
"""
from collections import defaultdict
from fractions import Fraction


class Solution:
    def maxPoints(self, points):
        if not points:
            return 0
        rst = 0
        for i in range(len(points)):
            same = 0
            rake2num = defaultdict(int)
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    same += 1
                elif points[i][0] == points[j][0]:
                    rake2num[None] += 1
                else:
                    rake = Fraction(points[i][1] - points[j][1]) / Fraction(points[i][0] - points[j][0])
                    rake2num[rake] += 1
            max_ = same + 1
            if rake2num:
                max_ += max(rake2num.values())
            rst = max(rst, max_)
        return rst


print(
    Solution().maxPoints(
[[0,0],[94911151,94911150],[94911152,94911151]]
    )
)
