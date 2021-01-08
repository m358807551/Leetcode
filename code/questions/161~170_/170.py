"""
https://leetcode-cn.com/problems/two-sum-iii-data-structure-design/
"""


class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.nums.append(number)
        self.nums.sort()

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        left = 0
        right = len(self.nums) - 1
        while left < right:
            if self.nums[left] + self.nums[right] > value:
                right -=1
            elif self.nums[left] + self.nums[right] < value:
                left += 1
            else:
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(3)
obj.add(1)
obj.add(2)
obj.add(3)
print(obj.find(3))
