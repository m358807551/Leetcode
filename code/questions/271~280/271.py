"""
https://leetcode-cn.com/problems/encode-and-decode-strings/
"""


class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        head = ','.join([str(len(line)) for line in strs])
        return head + ';' + ''.join(strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        head, stack = [], []
        for i, letter in enumerate(s):
            if letter == ';':
                if stack:
                    head.append(int(''.join(stack)))
                    stack = []
                break
            elif letter == ',':
                head.append(int(''.join(stack)))
                stack = []
            else:
                stack.append(letter)

        rst = []
        start = i + 1
        for i, count in enumerate(head):
            rst.append(s[start: start+count])
            start += count
        return rst


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# Your Codec object will be instantiated and called as such:
codec = Codec()

before = [
    ''
]
after = codec.decode(codec.encode(before))
for a, b in zip(before, after):
    if a != b:
        print(a)
        print(b)
        break
