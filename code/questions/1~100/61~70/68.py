"""
https://leetcode-cn.com/problems/text-justification
"""
class Solution(object):
    def fullJustify(self, words, maxwidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        rst = []
        line = []
        for word in words:
            if not self.is_valid(line + [word], maxwidth):
                left_space = maxwidth - len(''.join(line))
                spaces = self._split(left_space, len(line) - 1)
                rst.append(
                    self.justify(line, spaces)
                )
                line = [word]
            else:
                line.append(word)
        last_line = ' '.join(line)
        last_line += ' ' * (maxwidth - len(last_line))
        rst.append(last_line)
        return rst

    def is_valid(self, line, maxwidth):
        return len(''.join(line)) + len(line) - 1 <= maxwidth

    def _split(self, num, n):
        if n <= 1:
            return [num]
        else:
            x = num // n
            return self._split(num-x, n-1) + [x]

    def justify(self, line, spaces):
        spaces = [' '*num for num in spaces] + ['']
        rst = ''
        for word, space in zip(line, spaces):
            rst += word + space

        return rst

words = ["What","must","be","acknowledgment","shall","be"]
maxwidth = 16

print(
    # Solution()._split(5, 3
    # Solution().justify(['aa', 'aaaa', 'aa'], [3, 2])
    Solution().fullJustify(words, maxwidth)
)
