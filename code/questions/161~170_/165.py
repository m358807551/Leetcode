"""
https://leetcode-cn.com/problems/compare-version-numbers
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1, n2 = len(nums1), len(nums2)

        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 > i2:
                return 1
            elif i1 < i2:
                return -1
        return 0


print(
    Solution().compareVersion(
        '1',
        '0'
    )
)
