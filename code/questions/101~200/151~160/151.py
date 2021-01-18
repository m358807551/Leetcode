"""
https://leetcode-cn.com/problems/reverse-words-in-a-string
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 去掉多余的空格
        lis = []
        for letter in s:
            if letter == ' ':
                if lis and lis[-1] != ' ':
                    lis.append(letter)
            else:
                lis.append(letter)
        if lis and lis[-1] == ' ':
            lis.pop(-1)

        # 先全体逆置一下
        self.reverse(lis, 0, len(lis)-1)

        # 再逐个单词逆置
        start = end = 0
        while end < len(lis):
            while end < len(lis) and lis[end] != ' ':
                end += 1
            self.reverse(lis, start, end-1)
            start = end = end + 1

        return ''.join(lis)

    def reverse(self, lis, left, right):
        while left < right:
            lis[left], lis[right] = lis[right], lis[left]
            left += 1
            right -= 1


print(
    Solution().reverseWords(
        ' the sky is blue  '
    )
)
