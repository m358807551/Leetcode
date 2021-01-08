"""
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue, t = [], set()
        rst = 0
        for letter in s:
            while t and letter in t:
                t -= {queue.pop(0)}
            queue.append(letter)
            t |= {letter}
            rst = max(rst, len(queue))
        return rst


print(
    Solution().lengthOfLongestSubstring(
        'au'
        # 'bbbbb'
    )
)
