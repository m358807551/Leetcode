"""
https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        i = len(nums) // 2
        root = TreeNode(nums[i])
        root.left = self.sortedArrayToBST(nums[:i])
        root.right = self.sortedArrayToBST(nums[i+1:])
        return root


# 咪咕音乐的搜索词补全
import requests
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; Redmi 3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2693 MMWEBSDK/201001 Mobile Safari/537.36 MMWEBID/7731 MicroMessenger/7.0.20.1781(0x2700143B) Process/appbrand0 WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64"
}
rst = requests.get(
    'https://c.musicapp.migu.cn/v1.0/content/suggestrec.do?isCopyright=0&text=少',
    headers=headers,
    verify=True,
)
print(rst.json())
