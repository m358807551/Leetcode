"""
https://leetcode-cn.com/problems/implement-strstr/
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        next = [0]
        for i in range(1, len(needle)):
            k = next[i-1]
            while needle[k] != needle[i] and k > 0:
                k = next[k-1]
            next.append(k + 1 if needle[k] == needle[i] else 0)

        j = 0
        for i, letter in enumerate(haystack):
            while j and letter != needle[j]:
                j = next[j-1]
            if letter == needle[j]:
                if j == len(needle) - 1:
                    return i - j
                j += 1
            else:
                j = 0
        return -1

print(
    Solution().strStr(
"mississippi",
"issip"
    )
)
