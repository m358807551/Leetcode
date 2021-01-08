"""
https://leetcode-cn.com/problems/integer-to-english-words/
"""


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = (
            'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen '
            'Seventeen Eighteen Nineteen'
        ).split()
        d = {k: v for k, v in enumerate(d)}
        d.update({20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
                  90: 'Ninety'})

        for k, v in {1000000000: 'Billion', 1000000: 'Million', 1000: 'Thousand', 100: 'Hundred'}.items():
            if num >= k:
                if num % k == 0:
                    return self.numberToWords(num // k) + ' ' + v
                else:
                    return self.numberToWords(num // k) + ' ' + v + ' ' + self.numberToWords(num % k)
        else:
            if num in d:
                return d[num]
            return d[num//10*10] + ' ' + d[num % 10]


print(
    Solution().numberToWords(
        17
    )
)
'Five Hundred Sixty Seven Thousand'
