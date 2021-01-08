"""
https://leetcode-cn.com/problems/longest-common-prefix/
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        rst = ''
        for line in zip(*strs):
            x = set(line)
            if len(x) > 1:
                break
            rst += x.pop()
        return rst


print(
    Solution().longestCommonPrefix(
        ["flower","flow","flight"]
    )
)
