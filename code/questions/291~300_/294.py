"""
https://leetcode-cn.com/problems/flip-game-ii/
"""


class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)-1):
            if s[i] == s[i+1] =='+':
                if not self.canWin(s[:i] + '--' + s[i+2:]):
                    return True
        return False


print(
    Solution().canWin(
        '++++++'
    )
)
