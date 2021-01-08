"""
https://leetcode-cn.com/problems/3sum/
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        rst = set()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[i] > 0 or nums[right] < 0:
                    break

                if nums[i] + nums[left] + nums[right] == 0:
                    rst.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return list(rst)


print(
    Solution().threeSum(
        [-1, 0, 1, 2, -1, -4]
    )
)
