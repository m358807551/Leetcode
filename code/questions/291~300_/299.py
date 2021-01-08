"""
https://leetcode-cn.com/problems/bulls-and-cows/
"""
from collections import Counter


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = B = 0
        secret, guess = list(secret), list(guess)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
                secret[i] = guess[i] = '#'
        a = Counter(secret)
        b = Counter(guess)
        for letter, times in a.items():
            if letter == '#':
                continue
            B += min(times, b.get(letter, 0))
        return '{}A{}B'.format(A, B)

print(
    Solution().getHint(
        '1807',
        '7810'
    )
)
