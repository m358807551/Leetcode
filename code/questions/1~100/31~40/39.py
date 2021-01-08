"""
https://leetcode-cn.com/problems/combination-sum/
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.choices = sorted(candidates)
        self.rst = []
        self.backtrace([], target)
        return self.rst

    def backtrace(self, trace, target):
        if target == 0:
            self.rst.append(trace[:])
            return

        for choice in self.choices:
            if choice > target:
                break
            if trace and choice < trace[-1]:
                continue
            trace.append(choice)
            self.backtrace(trace, target-choice)
            trace.pop(-1)


print(
    Solution().combinationSum(
        candidates = [2,3,6,7], target = 7,
    )
)
