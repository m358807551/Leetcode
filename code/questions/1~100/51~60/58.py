"""
https://leetcode-cn.com/problems/length-of-last-word
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        rst = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if rst:
                    break
                else:
                    continue
            else:
                rst += 1

        return rst


print(
    Solution().lengthOfLastWord(
""
    )
)
