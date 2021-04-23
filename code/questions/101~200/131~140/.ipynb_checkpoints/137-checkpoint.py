"""
https://leetcode-cn.com/problems/single-number-ii
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1 << i):
                    count += 1
            if count % 3:
                rst |= (1 << i)

        if rst & (1 << 31):
            return -((1 << 32) -1 - (rst - 1))
        return rst


print(
    Solution().singleNumber([-2,-2,1,1,4,1,4,4,-5,-2])
)
