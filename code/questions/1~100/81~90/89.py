"""
https://leetcode-cn.com/problems/gray-code
"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        rst = [0]
        for i in range(1, pow(2, n)):
            rst.append(rst[-1] ^ (i & -i))
        return rst


print(
    Solution().grayCode(3)
)
