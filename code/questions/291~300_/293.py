"""
https://leetcode-cn.com/problems/flip-game/
"""


class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rst = []
        for i in range(len(s)-1):
            if s[i] == s[i+1] == '+':
                rst.append(s[: i] + '--' + s[i+2: ])
        return rst


print(
    Solution().generatePossibleNextMoves(
        '++++++'
    )
)
