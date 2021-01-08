"""
https://leetcode-cn.com/problems/count-primes
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0] * n
        for i in range(2, n):
            if nums[i] == 0:
                nums[i] = 1
                j = 2
                while i * j < n:
                    nums[i*j] = -1
                    j += 1
        return nums.count(1)


print(
    Solution().countPrimes(10)
)
