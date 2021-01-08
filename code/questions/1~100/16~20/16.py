"""
https://leetcode-cn.com/problems/3sum-closest/
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        rst = float('inf')
        for i in range(len(nums)-2):
            j, k = i + 1, len(nums)-1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == target:
                    return target
                if abs(sum3-target) < abs(rst-target):
                    rst = sum3
                if sum3 < target:
                    j += 1
                else:
                    k -= 1
        return rst




print(
    Solution().threeSumClosest(
[-1,2,1,-4],
1
    )
)
