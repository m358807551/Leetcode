"""
https://leetcode-cn.com/problems/missing-ranges/
"""


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = [lower-1] + nums + [upper+1]
        rst = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 2:
                rst.append(str(nums[i]-1))
            elif nums[i] - nums[i-1] > 2:
                rst.append('{}->{}'.format(nums[i-1]+1, nums[i]-1))
        return rst


nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99


print(
    Solution().findMissingRanges(nums, lower, upper)
)


"""
输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
输出: ["2", "4->49", "51->74", "76->99"]
"""
