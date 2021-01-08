"""
https://leetcode-cn.com/problems/shortest-palindrome/
"""

class Solution(object):
    def shortestPalindrome(self, s):
        if len(s) < 2:
            return s
        s2 = s + '#!' + s[::-1]
        next = [0] * len(s2)
        next[0] = 0
        next[1] = 1 if s2[0] == s2[1] else 0
        for j in range(2, len(s2)):
            k = next[j-1]
            while True:
                if s2[k] == s2[j]:
                    next[j] = k + 1
                    break
                if not k:
                    break
                k = next[k-1]
        return s[next[-1]:][::-1] + s

print(
    Solution().shortestPalindrome(
        'babbbabbaba'
    )
)
print('"ababbabbbabbaba"')
