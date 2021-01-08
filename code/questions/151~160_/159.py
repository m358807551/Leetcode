"""
https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/
"""
from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 2:
            return len(s)
        left = 0
        right = 1
        dic = defaultdict(int)
        dic[s[0]] = 1
        rst = 1

        while True:
            while right < len(s) and len(dic) < 3:
                dic[s[right]] += 1
                right += 1
            if len(dic) > 2 and right==len(s):
                rst = max(rst, right - left - 1)
                break
            elif len(dic) > 2:
                rst = max(rst, right - left -1)
            else:
                rst = max(rst, right - left)
                break

            while left < right and len(dic) > 2:
                dic[s[left]] -= 1
                if not dic[s[left]]:
                    dic.pop(s[left])
                left += 1

        return rst


print(
    Solution().lengthOfLongestSubstringTwoDistinct(
        'abc'
    )
)
