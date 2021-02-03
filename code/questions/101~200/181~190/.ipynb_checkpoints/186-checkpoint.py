"""
https://leetcode-cn.com/problems/reverse-words-in-a-string-ii/
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.append(' ')
        i, j = 0, 1
        n = len(s)
        while j < n:
            if s[j] == ' ':
                self.reverse(s, i, j-1)
                i = j+1
            j += 1

        s.pop(-1)
        self.reverse(s, 0, len(s)-1)

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

s = list('the sky is blue')
print(
    Solution().reverseWords(s)
)
print(s)
