"""
https://leetcode-cn.com/problems/candy
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        for i in range(n-1):
            if ratings[i+1] > ratings[i]:
                left[i+1] += left[i]
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                right[i-1] += right[i]
        rst = 0
        for i in range(n):
            rst += max(left[i], right[i])
        return rst



print(
    Solution().candy(
        [1, 2, 2]
    )
)
