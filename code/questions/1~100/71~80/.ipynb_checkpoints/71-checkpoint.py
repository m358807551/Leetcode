"""
https://leetcode-cn.com/problems/simplify-path
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for x in path.split('/'):
            if x in {'', '.'}:
                continue
            elif x == '..':
                if stack:
                    stack.pop(-1)
            else:
                stack.append(x)
        if not stack:
            return '/'
        return '/' + '/'.join(stack)


print(
    Solution().simplifyPath(
        '/a/./b/../../c/'
    )
)
