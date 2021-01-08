"""
https://leetcode-cn.com/problems/wiggle-sort/
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = len(nums) // 2
        if len(nums) % 2:
            mid += 1
        nums[::2], nums[1::2] = nums[: mid], nums[mid:]


def main():
    nums = [3,5,2,1,6]
    Solution().wiggleSort(nums)
    print(nums)


if __name__ == '__main__':
    main()
