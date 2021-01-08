"""
https://leetcode-cn.com/problems/trapping-rain-water/
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        queue = []
        rst = t = 0
        for num in height:
            if queue and num >= queue[0]:
                rst += t
                t = 0
                queue = []

            queue.append(num)
            t += queue[0] - num

        return rst + self.trap(queue[::-1])




print(
    Solution().trap(
        [4, 2, 3]
    )
)
