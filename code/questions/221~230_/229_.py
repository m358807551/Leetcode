"""
https://leetcode-cn.com/problems/majority-element-ii/
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        major, count = -1, 0
        for num in nums:
            if num == major:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 1
                    major = num

        second, count2 = -1, 0
        for num in nums:
            if num == major:
                continue
            if num == second:
                count2 += 1
            else:
                count2 -= 1
                if count2 < 0:
                    count2 = 1
                    second = num

        c1, c2 = 0, 0
        for num in nums:
            if num == major:
                c1 += 1
            elif num == second:
                c2 += 1

        rst = []
        if c1 > len(nums) // 3:
            rst.append(major)
        if c2 > len(nums) // 3:
            rst.append(second)
        return rst


print(
    Solution().majorityElement(
        [1, 1, 1, 2, 3, 4, 5, 6]
    )
)
