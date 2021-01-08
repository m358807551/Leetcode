"""
https://leetcode-cn.com/problems/summary-ranges
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        queue, stack = [], []
        for num in nums:
            if stack and (stack[-1]+1 != num):
                queue.append('{}->{}'.format(stack[0], stack[-1]) if len(stack) > 1 else str(stack[0]))
                stack = [num]
            else:
                stack.append(num)
        if stack:
            queue.append('{}->{}'.format(stack[0], stack[-1]) if len(stack) > 1 else str(stack[0]))
        return queue



print(
    Solution().summaryRanges(
[0,2,3,4,6,8,9]
    )
)
