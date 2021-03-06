# Leetcode

#### [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

##### 最简题解 [1.两数之和 Python三种解法总结](https://leetcode-cn.com/problems/two-sum/solution/1liang-shu-zhi-he-pythonsan-chong-jie-fa-7xo0/)

##### 最简代码

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [i, d[target - num]]
            d[num] = i
```

#### [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

##### 最简题解 [2. 两数相加，易懂解法，精炼解析](https://leetcode-cn.com/problems/add-two-numbers/solution/2-liang-shu-xiang-jia-yi-dong-jie-fa-jin-9obh/)

##### 代码

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return self.res(l1, l2, 0)

    def res(self, h1, h2, i):
        if (h1 is h2 is None) and (i == 0):
            return None
        val = i
        if h1:
            val += h1.val
        if h2:
            val += h2.val
        head = ListNode(val % 10)
        head.next = self.res(h1.next if h1 else None, h2.next if h2 else None,  val // 10)
        return head
```

#### [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

##### 最简题解 [画解算法：3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-jie-suan-fa-3-wu-zhong-fu-zi-fu-de-zui-chang-z/)

##### 最简代码

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rst, i, j = 0, 0, 0
        set_ = set()
        while True:
            while j < len(s) and (s[j] not in set_):
                set_.add(s[j])
                j += 1
            rst = max(rst, j - i)
            if j == len(s):
                break
                
            while s[j] in set_:
                set_.remove(s[i])
                i += 1
        return rst
```

#### [4. 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

##### 题解

###### 找有序数组的中位数

```
找到第(n+1)/2 个数 和第 (n+2)/2 个数，这俩数的平均值就是中位数;
这样可以避免区分数组长度是奇数还是偶数。
```

###### 转化为求数组第k位的问题

##### 代码

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        v1 = self.find_k(nums1, 0, nums2, 0, (m+n+1)//2)
        v2 = self.find_k(nums1, 0, nums2, 0, (m+n+2)//2)
        return (v1 + v2) / 2.0
        

    def find_k(self, nums1, i, nums2, j, k):
        m, n = len(nums1), len(nums2)
        if i >= m:
            return nums2[j+k-1]
        elif j >= n:
            return nums1[i+k-1]

        if k == 1:
            return min(nums1[i], nums2[j])

        mid1 = nums1[i+k//2-1] if i+k//2-1 < m else float("inf")
        mid2 = nums2[j+k//2-1] if j+k//2-1 < n else float("inf")
        if mid1 < mid2:
            return self.find_k(nums1, i+k//2, nums2, j, k-k//2)
        else:
            return self.find_k(nums1, i, nums2, j+k//2, k-k//2)
```

##### 参考：[综合百家题解，总结最清晰易懂的二分题解！](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/zong-he-bai-jia-ti-jie-zong-jie-zui-qing-xi-yi-don/)

#### [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

##### 题解

```
这套题挂羊头卖狗肉，官方分类在动态规划里，实际上用动态规划写出来时间上要么超时，要么倒数。
用更简单的方法反而效率不错：遍历每个字符，不断两边扩散成最长的回文串，记录最长的回文串就是答案。
```

##### 代码

```python
class Solution(object):
    def longestPalindrome(self, s):
        left, right = 0, 0
        for i in range(len(s)):
            a, b = self.expand(s, i, i)
            if b - a > right - left:
                left, right = a, b
            a, b = self.expand(s, i, i+1)
            if b - a > right - left:
                left, right = a, b
        return s[left: right+1]
    
    def expand(self, s, i, j):
        while i>=0 and j<len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return i+1, j-1
```

#### [6. Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion/)

#### 最简题解 [Z 字形变换（清晰图解）](https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/)

#### 最简代码 

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)
```

#### [7. 整数反转](https://leetcode-cn.com/problems/reverse-integer/)

##### 题解

```
每次取各位数字进行运算。
```

##### 代码

```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        positive = True if x >= 0 else False
        x = abs(x)
        rst = 0
        while x:
            rst = rst * 10 + x % 10
            x = x // 10
        rst = rst if positive else -rst
        return rst if (-pow(2, 31)<= rst <= pow(2, 31)-1) else 0
```

#### [8. 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/)

##### 题解

```
这是一道偏工程的题目，没有什么高深的算法，就是按部就班的来就行。

1. 去掉前导空格
2. 判断正负号
3. 算出数字
4. 数字太大或太小就限定在一定范围内。
```

##### 代码

```python
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        rst, positive = 0, True
        if i < len(s) and s[i] == '-':
            positive = False
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
        
        while (i < len(s)) and ('0' <= s[i] <= '9'):
            rst = rst * 10 + int(s[i])
            i += 1
        
        if not positive:
            rst = -rst
        
        if rst < -pow(2, 31):
            rst = -pow(2, 31)
        
        if rst > (pow(2, 31) - 1):
            rst = pow(2, 31)
        
        return rst
```

#### [9. 回文数](https://leetcode-cn.com/problems/palindrome-number/)

##### 题解

```
先把数字转成字符串，再判断字符串是否回文。
```

##### 代码

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]
```

#### [10. 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)

##### 题解

```
这道题的标签虽然有回溯算法，但是就是一个典型的动态规划问题，也是力扣第一道动态规划困难题。

dp[i][j] 表示 s[:i] 和 p[:j] 是否正则匹配。
```

##### 代码

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [ [False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if s[i-1] == p[j-2] or "." == p[j-2]:
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
                else:
                    if s[i-1] == p[j-1]:
                        dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
```

#### [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)

##### 最简题解 [盛最多水的容器（双指针法，易懂解析，图解）](https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/)

##### 最简代码

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        rst = 0
        while i < j:
            rst = max(rst, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return rst
```

#### [12. 整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman/)

##### 题解

```
从大到小列出所有可能的符号，不段连接字符串。
```

##### 代码

```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        lis = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        rst = ""
        while num:
            for n, s in lis:
                if num >= n:
                    rst += s
                    num -= n
                    break
        return rst
```

#### [13. 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)

##### 题解

```
跟12题一样的。
```

##### 代码

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        rst = 0
        while s:
            for num, letter in lis:
                if s[:len(letter)] == letter:
                    rst += num
                    s = s[len(letter):]
                    break
        return rst
```

#### [14. 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)

##### 最简题解 [14. 最长公共前缀 这种题在python面前就是弟弟！](https://leetcode-cn.com/problems/longest-common-prefix/solution/14-zui-chang-gong-gong-qian-zhui-zhe-cho-uwrm/)

##### 最简代码

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        rst = ""
        for line in zip(*strs):
            x = set(line)
            if len(x) > 1:
                break
            rst += x.pop()
        return rst
```

#### [16. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/)

##### 最简题解 [画解算法：16. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/solution/hua-jie-suan-fa-16-zui-jie-jin-de-san-shu-zhi-he-b/)

##### 最简代码

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        rst = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if abs(sum_ - target) < abs(rst - target):
                    rst = sum_
                if sum_ > target:
                    k -= 1
                else:
                    j += 1
        return rst
```

#### [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

##### 最简题解 [回溯+队列 图解](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/hui-su-dui-lie-tu-jie-by-ml-zimingmeng/)

##### 最简代码

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.rst = []
        self.backtrace("", digits)
        return self.rst
    
    def backtrace(self, trace, digits):
        if not digits:
            if trace:
                self.rst.append(trace)
            return
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        for letter in d[digits[0]]:
            self.backtrace(trace+letter, digits[1:])
```

#### [18. 四数之和](https://leetcode-cn.com/problems/4sum/)

##### 最简题解 [双指针解法。参照三数之和，嗝。](https://leetcode-cn.com/problems/4sum/solution/shuang-zhi-zhen-jie-fa-can-zhao-san-shu-zhi-he-ge-/)

##### 最简代码

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rst = set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left, right = j + 1, len(nums)-1
                while left < right:
                    sum_ = nums[left] + nums[right] + nums[i] + nums[j]
                    if sum_ == target:
                        rst.add((nums[left], nums[right], nums[i], nums[j]))
                        right -= 1
                    elif sum_ < target:
                        left += 1
                    else:
                        right -= 1
        return list(rst)
```

#### [19. 删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

##### 题解

```
关键在找到要删除节点的前一个节点。

用两个指针，快指针先走n+1步，然后接下来每回合两个指针各向后走一步，直到快指针指向null为止，此时慢指针指向要删除节点的前一个节点。

记得手动加一个辅助头节点。
```

##### 代码

```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        t = ListNode(next=head)
        fast = slow = t
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return t.next
```

#### [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

##### 题解

```
判断括号的有效性是栈的常用功能。
```

##### 代码

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {')': '(', "]": "[", "}": "{"}
        for letter in s:
            if letter in d.values():
                stack.append(letter)
            elif stack and (stack[-1] == d[letter]):
                stack.pop(-1)
            else:
                return False
        return len(stack) == 0
```

#### [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

##### 最简题解 [一看就会，一写就废？详解递归](https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/)

##### 最简代码 

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 and l2) is None:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

#### [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)

##### 题解

```
回溯函数中:
    left: 还可以用多少个左括号
    right: 还可以用多少个右括号
```

##### 代码

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.rst = []
        self.backtrace([], n, n)
        return self.rst

    def backtrace(self, trace, left, right):
        if left == right == 0:
            self.rst.append(''.join(trace))
            return
        
        if left:
            trace.append("(")
            self.backtrace(trace, left-1, right)
            trace.pop(-1)
        
        if left < right:
            trace.append(")")
            self.backtrace(trace, left, right-1)
            trace.pop(-1)
```

#### [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

##### 最简题解 [两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-91/)

##### 最简代码

```python
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            rst = head.next
            head.next.next, head.next = head, self.swapPairs(head.next.next)
            return rst
        else:
            return head
```

#### [25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)

##### 题解

```
链表题中唯一一个困难题目。

先实现: 反转链表前 k 个元素。

递归在链表中很好用。
```

##### 代码

```python

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not self.enough(head, k):
            return head
        rst = self.reverseK(head, k)
        if self.q:
            head.next = self.reverseKGroup(self.q, k)
        return rst
        
    def reverseK(self, head, k):
        if k == 1:
            self.q = head.next
            return head
        else:
            rst = self.reverseK(head.next, k-1)
            head.next.next, head.next = head, None
            return rst
    
    def enough(self, head, k):
        if not k:
            return True
        if not head:
            return False
        return self.enough(head.next, k-1)
```

#### [26. 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

##### 最简题解 [删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shan-chu-pai-xu-shu-zu-zhong-de-zhong-fu-xiang-by-/)

##### 最简代码：

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums:
            if (not i) or (num != nums[i-1]):
                nums[i] = num
                i += 1
        return i
```

#### [27. 移除元素](https://leetcode-cn.com/problems/remove-element/)

##### 最简题解 [双指针Python](https://leetcode-cn.com/problems/remove-element/solution/shuang-zhi-zhen-python-by-distracted-hod-7nyc/)

##### 最简代码

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i
```

#### [28. 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/)

##### 最简题解 [一行python](https://leetcode-cn.com/problems/implement-strstr/solution/yi-xing-python-by-distracted-hodgkinlap-dbsw/)

##### 最简代码

```python
class Solution:
    def strStr(self, haystack, needle):
        return 0 if needle == "" else haystack.find(needle)
```

#### [30. 串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)

##### 最简题解 [串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/solution/chuan-lian-suo-you-dan-ci-de-zi-chuan-by-powcai/)

##### 最简代码

```python
from collections import Counter


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not(s and words):
            return []
        k = len(words[0])
        n = len(words) * k
        words = Counter(words)
        
        rst = []
        for i in range(len(s)):
            t = s[i:i+n]
            lis = [t[j:j+k] for j in range(0, n, k)]
            if Counter(lis) == words:
               rst.append(i)
        return rst
```

#### [31. 下一个排列](https://leetcode-cn.com/problems/next-permutation/)

##### 最简题解：[下一个排列算法详解：思路+推导+步骤，看不懂算我输！](https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/)

##### 最简代码

```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        nums[i:] = sorted(nums[i:])
                        break
                break
        else:
            nums[:] = nums[::-1]
```

#### [32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)

##### 题解

```
这道题虽说分类在困难的动态规划，但还是有大神能用栈以接近简单难度的方法破解出来。

关键是加一个标志位，以及每次计算长度方式：右括号的索引 - 弹出一个元素后此时栈顶的值
```

##### 代码

```python
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        rst = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                stack.pop(-1)
                if stack:
                    rst = max(rst, i - stack[-1])
                else:
                    stack.append(i)
        return rst
```

参考: [「手画图解」剖析两种题解：利用栈、动态规划](https://leetcode-cn.com/problems/longest-valid-parentheses/solution/shou-hua-tu-jie-zhan-de-xiang-xi-si-lu-by-hyj8/)

#### [33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)

##### 题解

```
1. 将数组分成左右两部分。

2. 左部分有序？
    2.1 目标值在左部分里：选择左部分
    2.2 否则选择右部分

3. 否则：
    3.1 目标值在有部分里：选择右部分
    3.2 否则选择左部分
```

##### 代码

```python
class Solution(object):
    def search(self, nums, target):
        i, j = 0, len(nums)-1
        while i < j:
            mid = i + (j-i)//2
            if nums[i] <= nums[mid]:  #左有序
                if nums[i] <= target <= nums[mid]:
                    j = mid
                else:
                    i = mid + 1
            else: 
                if nums[mid+1] <= target <=nums[j]:
                    i = mid + 1
                else:
                    j = mid
                        
        return i if nums[i] == target else -1
```

#### [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

##### 题解

```
找等于元素的第一个位置 a，和大于元素的第一个位置b。

最后返回 [a, b-1]
```

##### 代码

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return -1, -1
        i, j = 0, len(nums)-1
        while i < j:
            mid = i + (j-i)//2
            if target <= nums[mid]:
                j = mid
            else:
                i = mid+1
        left = i if nums[i] == target else -1
        if left == -1:
            return (-1, -1)
        
        i, j = 0, len(nums) -1 
        while i < j:
            mid = i + (j-i)//2
            if target < nums[mid]:
                j = mid
            else:
                i = mid + 1
        
        right = i if nums[i] == target else i - 1
        
        return left, right
```

#### [35. 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)

##### 题解

```
注意两种特殊情况，需要特殊处理。
  1. nums为空
  2. target 比 nums中最大的元素还大
```

##### 代码

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target > nums[-1]:
            return len(nums)
        i, j = 0, len(nums)-1
        while i < j:
            mid = i + (j-i)//2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        return i
```

#### [36. 有效的数独](https://leetcode-cn.com/problems/valid-sudoku/)

##### 最简题解 [36. 简单想法，最优思路：就按照从左往右、从上往下的顺序遍历一次board，完成3个条件的检验](https://leetcode-cn.com/problems/valid-sudoku/solution/36-jiu-an-zhao-cong-zuo-wang-you-cong-shang-wang-x/)

##### 最简代码

```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = 9
        for i in range(n):
            line = board[i]
            if not self.is_valid(line):
                return False
        
        for j in range(n):
            line = [board[i][j] for i in range(n)]
            if not self.is_valid(line):
                return False

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                line = [board[k][l] for k in range(i, i+3) for l in range(j, j+3)]
                if not self.is_valid(line):
                    return False
        return True
        
    def is_valid(self, line):
        s = set()
        for letter in line:
            if letter == ".":
                continue
            if letter in s:
                return False
            s.add(letter)
        return True
```

#### [37. 解数独](https://leetcode-cn.com/problems/sudoku-solver/)

##### 最简题解 [37. 解数独：回溯法](https://leetcode-cn.com/problems/sudoku-solver/solution/37-jie-shu-du-hui-su-fa-by-jue-qiang-zha-bhqh/)

##### 最简代码

```python
from copy import deepcopy


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.rst = None
        self.backtrace(board, 0, 0)
        board[:] = self.rst
    
    def backtrace(self, board, i, j):
        if i >= 9:
            self.rst = deepcopy(board)
            return
        if board[i][j] != ".":
            self.backtrace(board, i+(j+1)//9, (j+1)%9)
            return
        for num in range(1, 10):
            num = str(num)
            if num in board[i]:
                continue
            if num in [board[i][j] for i in range(9)]:
                continue
            r, c = (i//3)*3, (j//3)*3
            if num in [board[k][l] for k in range(r, r+3) for l in range(c, c+3)]:
                continue
            board[i][j] = num
            self.backtrace(board, i+(j+1)//9, (j+1)%9)
            board[i][j] = "."
```

#### [38. 外观数列](https://leetcode-cn.com/problems/count-and-say/)

##### 最简题解 [循环和递归两种解法，递归效率高](https://leetcode-cn.com/problems/count-and-say/solution/xun-huan-he-di-gui-liang-chong-jie-fa-di-oof8/)

##### 最简代码

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        t = self.countAndSay(n-1)
        rst = ""
        char, count = "", 0
        for letter in t:
            if letter == char:
                count += 1
            else:
                if count:
                    rst += str(count) + char
                char = letter
                count = 1
        if count:
            rst += str(count) + char
        return rst
```

#### [39. 组合总和](https://leetcode-cn.com/problems/combination-sum/)

##### 题解

```
典型的回溯问题，就是注意一下为了防止重复解，每个解限制一下后面的数必须大于等于前面的数即可。
```

##### 代码

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums = sorted(candidates)
        self.rst = []
        self.backtrace([], target)
        return self.rst
    
    def backtrace(self, trace, target):
        if target == 0:
            self.rst.append(trace[:])
            return
        
        for num in self.nums:
            if trace and (trace[-1] > num):
                continue
            if num <= target:
                trace.append(num)
                self.backtrace(trace, target-num)
                trace.pop(-1)
            else:
                break
```

#### [40. 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii/)

##### 题解

```
跟上一题几乎相同~~
```

##### 代码
```python
from collections import Counter


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.rst = []
        count = Counter(candidates)
        self.backtrace([], count, target)
        return self.rst
    
    def backtrace(self, trace, count, target):
        if target == 0:
            self.rst.append(trace[:])
        
        for num in count:
            if trace and trace[-1] > num:
                continue
            if count[num] and num <= target:
                trace.append(num)
                count[num] -= 1
                self.backtrace(trace, count, target-num)
                trace.pop(-1)
                count[num] += 1
        
```

#### [41. 缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/)

##### 最简题解: [缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode-solution/)

##### 最简代码

```python
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
```

#### [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)

##### 最简题解: [单调栈O(n)解决，动图预警🎶🎵](https://leetcode-cn.com/problems/trapping-rain-water/solution/dan-diao-zhan-jie-jue-jie-yu-shui-wen-ti-by-sweeti/)

##### 最简代码

```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rst, stack = 0, []
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                if len(stack) >= 2:
                    rst += min(
                        height[i]-height[stack[-1]], 
                        height[stack[-2]]-height[stack[-1]]
                    ) * (i-stack[-2]-1)
                stack.pop(-1)
            stack.append(i)
        return rst
```

#### [43. 字符串相乘](https://leetcode-cn.com/problems/multiply-strings/)

##### 题解

```
列竖式，算乘法。
```

##### 代码

```python
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        m, n = len(num1), len(num2)
        rst = [0] * (m + n)
        for j in range(n):
            for i in range(m):
                t = int(num1[i]) * int(num2[j])
                rst[i+j] += t % 10
                rst[i+j+1] += t // 10
        for i in range(len(rst)-1):
            rst[i+1] += rst[i] // 10
            rst[i] = rst[i] % 10
        
        rst = ''.join([str(x) for x in rst[::-1]])
        rst = rst.lstrip('0')
        return rst if rst else '0'
```

#### [44. 通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/)

##### 最简题解 [通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/solution/tong-pei-fu-pi-pei-by-leetcode-solution/)

##### 最简代码

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]

        dp[0][0] = True
        for i in range(1, n+1):
            if p[i-1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False

        return dp[m][n]
```

#### [45. 跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/)

##### 最简题解 [详细通俗的思路分析，多解法](https://leetcode-cn.com/problems/jump-game-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-10/)

##### 最简代码

```python
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst, end, most_right = 0, 0, 0
        for i in range(len(nums)-1):
            most_right = max(most_right, i + nums[i])
            if i == end:
                end = most_right
                rst += 1
        return rst
```

#### [46. 全排列](https://leetcode-cn.com/problems/permutations/)

##### 题解

```
回溯经典问题。
```

##### 代码

```python
from collections import Counter

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counts, self.n = Counter(nums), len(nums)
        self.rst = []
        self.backtrace([], counts)
        return self.rst
    
    def backtrace(self, trace, counts):
        if len(trace) == self.n:
            self.rst.append(trace[:])
            return
        for num in counts:
            if counts[num]:
                trace.append(num)
                counts[num] -= 1
                self.backtrace(trace, counts)
                trace.pop(-1)
                counts[num] += 1
```

#### [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)

##### 题解

```
跟上一题的代码完全一样。
```

##### 代码

```python
from collections import Counter


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.rst, self.n, counts = [], len(nums), Counter(nums)
        self.backtrace([], counts)
        return self.rst
    
    def backtrace(self, trace, counts):
        if len(trace) == self.n:
            self.rst.append(trace[:])
            return
        
        for num in counts:
            if counts[num]:
                trace.append(num)
                counts[num] -= 1
                self.backtrace(trace, counts)
                trace.pop(-1)
                counts[num] += 1
```

#### [48. 旋转图像](https://leetcode-cn.com/problems/rotate-image/)

##### 最简题解 

```
方阵向右循环90°等价于：
1. 先沿主对角线对折
2. 每一行逆序
```

##### 最简代码

```python
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i] = matrix[i][::-1]
```

#### [49. 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)

##### 最简题解 [字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/solution/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/)

##### 最简代码

```python
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            d[key].append(s)
        return list(d.values())
```

#### [50. Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)

##### 题解

```
每次对半乘，存一下中间结果。
```

##### 代码

```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1. / self.myPow(x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2: # 是奇数
            t = self.myPow(x, (n-1)//2)
            return t * t * x
        else:  # n 是偶数
            t = self.myPow(x, n//2)
            return t * t
```

#### [51. N 皇后](https://leetcode-cn.com/problems/n-queens/)

##### 题解

```
回溯问题的题解都是相似的。。纯回溯问题中也就N皇后问题是个困难题，但是套模型仍然很简单。
```

##### 代码

```python
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        trace = [ ['.'] * n for _ in range(n)]
        self.rst = []
        self.backtrace(trace, 0)
        return self.rst
    
    def backtrace(self, trace, i):
        if i == len(trace):
            self.rst.append([
                "".join(line)
                for line in trace
            ])
            return
        for j in range(len(trace)):
            if self.is_valid(trace, i, j):
                trace[i][j] = 'Q'
                self.backtrace(trace, i+1)
                trace[i][j] = '.'
            
    def is_valid(self, trace, i, j):
        # 纵向
        for k in range(i):
            if trace[k][j] == 'Q':
                return False

        # 左上
        k = 0
        while (0<=i-k) and (0<=j-k):
            if trace[i-k][j-k] == 'Q':
                return False
            k += 1

        # 右上
        k = 0
        while (0<=i-k) and (j+k < len(trace)):
            if trace[i-k][j+k] == 'Q':
                return False
            k += 1
        
        return True
```

#### [52. N皇后 II](https://leetcode-cn.com/problems/n-queens-ii/)

##### 题解

```
上一题改两行代码.
```

##### 代码

```python
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        trace = [ ['.'] * n for _ in range(n)]
        self.rst = 0
        self.backtrace(trace, 0)
        return self.rst
    
    def backtrace(self, trace, i):
        if i == len(trace):
            self.rst += 1
            return
        for j in range(len(trace)):
            if self.is_valid(trace, i, j):
                trace[i][j] = 'Q'
                self.backtrace(trace, i+1)
                trace[i][j] = '.'
            
    def is_valid(self, trace, i, j):
        # 纵向
        for k in range(i):
            if trace[k][j] == 'Q':
                return False

        # 左上
        k = 0
        while (0<=i-k) and (0<=j-k):
            if trace[i-k][j-k] == 'Q':
                return False
            k += 1

        # 右上
        k = 0
        while (0<=i-k) and (j+k < len(trace)):
            if trace[i-k][j+k] == 'Q':
                return False
            k += 1
        
        return True
```

#### [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

##### 最简题解 [【Dp思路】子序列类问题的通解](https://leetcode-cn.com/problems/maximum-subarray/solution/dpsi-lu-zi-xu-lie-lei-wen-ti-de-tong-jie-de8x/)

##### 最简代码

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = float("-inf")
        t = 0
        for num in nums:
            t += num
            rst = max(rst, t)
            if t < 0:
                t = 0
        return rst
```

#### [54. 螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix/)

##### 最简题解 [展开"蛋糕卷"](https://leetcode-cn.com/problems/spiral-matrix/solution/zhan-kai-dan-gao-juan-by-nanaglutamate-dc7u/)

##### 最简代码

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rst = []
        while matrix:
            rst.extend(matrix[0][:])
            matrix = matrix[1:]
            matrix = list(zip(*matrix))[::-1]
        return rst
```

#### [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)

##### 最简题解 [Python击败97%，看不懂你锤我](https://leetcode-cn.com/problems/jump-game/solution/pythonji-bai-97kan-bu-dong-ni-chui-wo-by-mo-lan-4/)

##### 最简代码

```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        most_right = 0
        for i in range(len(nums)-1):
            if most_right < i:
                break
            most_right = max(most_right, i + nums[i])
        return len(nums)-1 <= most_right
```

#### [56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/)

##### 最简题解 [合并区间]([56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/))

##### 最简代码

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        rst = []
        for x in intervals:
            if not rst:
                rst.append(x)
            elif rst[-1][1] < x[0]:
                rst.append(x)
            else:
                rst[-1][1] = max(rst[-1][1], x[1])
        return rst
```

#### [57. 插入区间](https://leetcode-cn.com/problems/insert-interval/)

##### 最简题解 [直接调用上一题的就好啦](https://leetcode-cn.com/problems/insert-interval/solution/zhi-jie-diao-yong-shang-yi-ti-de-jiu-hao-nso9/)

##### 最简代码

```python
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        stack = []
        intervals.append(newInterval)
        intervals.sort()
        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue

            if stack[-1][1] < interval[0]:
                stack.append(interval)
            else:
                stack[-1][1] = max(stack[-1][1], interval[1])
        return stack
```

#### [58. 最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word/)

##### 最简题解 [Python字符串](https://leetcode-cn.com/problems/length-of-last-word/solution/pythonzi-fu-chuan-by-distracted-hodgkinl-mrb9/)

##### 最简代码

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1]) if s.strip() else 0
```

#### [59. 螺旋矩阵 II](https://leetcode-cn.com/problems/spiral-matrix-ii/)

##### 最简题解 

```
设定上下左右4个边界，不断缩小边界。
```

##### 最简代码

```python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        up, down, left, right = 0, n-1, 0, n-1
        num = 1
        rst = [[0] * n for _ in range(n)]
        while True:
            if not(up<=down and left<=right): break
            for i in range(left, right+1):
                rst[up][i] = num
                num += 1
            up += 1
            
            if not(up<=down and left<=right): break
            for i in range(up, down+1):
               rst[i][right] = num
               num += 1
            right -= 1
            
            if not(up<=down and left<=right): break
            for i in range(right, left-1, -1):
               rst[down][i] = num
               num += 1
            down -= 1
            
            if not(up<=down and left<=right): break
            for i in range(down, up-1, -1):
               rst[i][left] = num
               num += 1
            left += 1
        
        return rst
```

#### [60. 排列序列](https://leetcode-cn.com/problems/permutation-sequence/)

##### 题解

见 [python3 超详细多解法](https://leetcode-cn.com/problems/permutation-sequence/solution/python3-chao-xiang-xi-duo-jie-fa-by-ting-ting-28-3/)

##### 代码

```python
import math


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        rst, k = '', k-1
        s = [str(x) for x in range(1, n+1)]
        while s:
            n = math.factorial(len(s)-1)
            rst += s.pop(k // n)
            k = k % n
        return rst
```

#### [61. 旋转链表](https://leetcode-cn.com/problems/rotate-list/)

##### 题解

```
1. 将链表收尾相连，形成一个环

2. 找到第 链表的长度 - k - 1 个节点，从这里断开，返回新的链表头
```

##### 代码

```python
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        n = self.get_len(head)
        k = k % n
        
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = head
        
        p = head
        for _ in range(n-k-1):
            p = p.next
        rst = p.next
        p.next = None
        return rst
    
    def get_len(self, head):
        if not head:
            return 0
        return self.get_len(head.next) + 1
```

#### [62. 不同路径](https://leetcode-cn.com/problems/unique-paths/)

##### 题解

```
基础的动态规划题目。
```

##### 代码

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [ [1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
```

#### [63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)

##### 题解

```
跟题目62相似，只需做一点修改。
```

##### 代码

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [ [0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
```

#### [64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)

##### 题解

```
连做了 62,63,64，我怀疑我精通动态规划了。😺
```

##### 代码

```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [ [0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
```

#### [65. 有效数字](https://leetcode-cn.com/problems/valid-number/)

##### 题解

```
没有高深的算法，还是考验细心的题目，在纸上画出正确的状态机就能轻松过。
```

##### 代码

```python
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            0: {"+": 1, "-": 1, "9": 2, ".": 3},
            1: {"9": 2, ".": 3},
            2: {"9": 2, "e": 5, ".": 4},
            3: {"9": 4},
            4: {"9": 4, "e": 5},
            5: {"9": 6, "+": 7, "-": 7},
            6: {"9": 6},
            7: {"9": 6}
        }
        final_states = {2, 4, 6}
        state = 0
        for letter in s:
            letter = letter.lower()
            if '0' <= letter <= '9':
                letter = '9'
            state = d[state].get(letter)
            if state is None:
                return False
        return state in final_states
```

#### [66. 加一](https://leetcode-cn.com/problems/plus-one/)

##### 最简题解 [Java 数学解题](https://leetcode-cn.com/problems/plus-one/solution/java-shu-xue-jie-ti-by-yhhzw/)

##### 最简代码

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        i = len(digits)-1
        while i > 0 and digits[i] == 10:
            digits[i] = 0
            digits[i-1] += 1
            i -= 1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits
```

#### [67. 二进制求和](https://leetcode-cn.com/problems/add-binary/)

##### 题解

```
用一个数组存计算结果，最后将数组转成字符串。
```

##### 代码

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a[::-1], b[::-1]
        rst = [0] * (max(len(a), len(b)) + 1)
        for i in range(max(len(a), len(b))):
            rst[i] += int(a[i]) if i < len(a) else 0
            rst[i] += int(b[i]) if i < len(b) else 0
        for i in range(len(rst)-1):
            if rst[i] > 1:
                rst[i] = rst[i] - 2
                rst[i+1] += 1
        rst = "".join([str(x) for x in rst])
        return rst[::-1].lstrip("0") or "0"
```

#### [68. 文本左右对齐](https://leetcode-cn.com/problems/text-justification/)

##### 最简题解 

##### 最简代码

```python
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
```


#### [69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)

##### 题解

```
本质是二分查找，查找满足 i * i >= x 的第一个位置。
```

##### 代码

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i, j = 0, x
        while i < j:
            mid = i + (j-i)//2
            if mid * mid < x:
                i = mid + 1
            else:
                j = mid
        return i if i * i == x else i-1
```

#### [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

##### 题解

```
Leetcode前两百道题目里有19道动态规划，19个动态规划里只有两个难度是简单，爬楼梯是其中一道。
```

##### 代码

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
```

#### [71. 简化路径](https://leetcode-cn.com/problems/simplify-path/)

##### 最简题解：[Python 4 lines](https://leetcode-cn.com/problems/simplify-path/solution/python-4-line-by-qqqun902025048/)

##### 最简代码

```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for x in path.split("/"):
            if not x:
                continue
            elif x == '.':
                continue
            elif x == '..':
                if stack:
                    stack.pop(-1)
            else:
                stack.append(x)
        return '/' + '/'.join(stack)
```

#### [72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)

##### 题解

```
状态转移方程好写，就是怎么初始化困难些。
```

##### 代码

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not(word1 and word2):
            return len(word1) or len(word2)
        
        m, n = len(word1), len(word2)
        dp = [[0] * n for _ in range(m)]
        
        f = False
        for i in range(m):
            if word1[i] == word2[0]:
                f = True
            dp[i][0] = i if f else i + 1
        
        f = False
        for j in range(n):
            if word2[j] == word1[0]:
                f = True
            dp[0][j] = j if f else j + 1
        
        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
        return dp[-1][-1]
```

#### [73. 矩阵置零](https://leetcode-cn.com/problems/set-matrix-zeroes/)

##### 最简题解 [C++ | 图解 | 找个数字“借尸还魂” | O(1)空间](https://leetcode-cn.com/problems/set-matrix-zeroes/solution/c-tu-jie-zhao-ge-shu-zi-jie-shi-huan-hun-c1gh/)

##### 最简代码

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k]!=0: matrix[i][k] = None
                    for k in range(m):
                        if matrix[k][j]!=0: matrix[k][j] = None
        for i in range(m):
            for j in range(n):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
```

#### [74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)

##### 题解

```
从矩阵的右上角开始移动：

1. 目标值 == 目标值就返回
2. 目标值 < 当前值 就向左移动
3. 目标值 > 当前值 就向下移动
```

##### 代码

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False
```

#### [75. 颜色分类](https://leetcode-cn.com/problems/sort-colors/)

##### 最简题解 [C++8行优美代码！](https://leetcode-cn.com/problems/sort-colors/solution/c8xing-you-mei-dai-ma-by-xiaohu9527-fifj/)

##### 最简代码

```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)-1
        while True:
            for k in range(i, j+1):
                if nums[k] == 0:
                    nums[k], nums[i] = nums[i], nums[k]
                    i += 1
                    break
                elif nums[k] == 2:
                    nums[k], nums[j] = nums[j], nums[k]
                    j -= 1
                    break
            else:
                break
```

#### [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

##### 最简题解 [c++ 滑动窗口-z](https://leetcode-cn.com/problems/minimum-window-substring/solution/c-hua-dong-chuang-kou-z-by-zrita-g9bg/)

##### 最简代码

```python
from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        x, y = 0, 0
        count_t = Counter(t)
        d = defaultdict(int)
        need = set(count_t.keys())
        
        i, j = 0, 0
        while j < len(s):
            while j < len(s) and need:
                letter = s[j]
                j += 1
                d[letter] += 1
                if d[letter] >= count_t[letter]:
                    need -= {letter}
            while (i < j) and (not need):
                letter = s[i]
                i += 1
                d[letter] -= 1
                if (letter in count_t) and (d[letter] < count_t[letter]):
                    if (j-(i-1) < y -x) or (x == y == 0):
                        x, y = i-1, j
                    need.add(letter)
        return s[x:y]
```

#### [77. 组合](https://leetcode-cn.com/problems/combinations/)

##### 题解

```
回溯题题解好像都一样的~
```

##### 代码

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.n, self.k = n, k
        self.rst = []
        self.backtrace([])
        return self.rst
    
    def backtrace(self, trace):
        if len(trace) == self.k:
            self.rst.append(trace[:])
            return
        start = (trace[-1] + 1) if trace else 1
        for num in range(start, self.n+1):
            trace.append(num)
            self.backtrace(trace)
            trace.pop(-1)
```

#### [78. 子集](https://leetcode-cn.com/problems/subsets/)

##### 最简题解 [回溯算法](https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/)

##### 最简代码

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = [[]]
        for num in nums:
            rst.extend([x+[num] for x in rst])
        return rst
```

#### [79. 单词搜索](https://leetcode-cn.com/problems/word-search/)

##### 题解

```
这道题目的测试用例更改过，同样的代码之前300ms现在需要3000+ms，所以看到代码执行速度只超越5%的人不要方，这是正常的。

本题还有两个跟其它回溯题目不一样的地方:
1. 以前的回溯题需要一个个收集可能的结果保存下来，而这道题只要有了确定的答案，就直接返回，不再进行其它情况的寻找。表现在代码上，就是backtrace函数有了返回值(其它题目都返回None.)
2. 之前的题目都是在 调用backtrace 前确定参数的有效性，而本题目需要在backtrace函数的开头，确定传入的参数是否是合法的。
```

##### 代码

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrace(board, word, i, j, 0):
                    return True
        return False
    
    def backtrace(self, board, word, i, j, k):
        if k == len(word):
            return True
        m, n = len(board), len(board[0])
        if not((0 <= i < m) and (0 <= j < n)):
            return False
        if board[i][j] != word[k]:
            return False
        
        board[i][j] = '0'
        if (
            self.backtrace(board, word, i+1, j, k+1) 
            or self.backtrace(board, word, i-1, j, k+1)
            or self.backtrace(board, word, i, j+1, k+1)
            or self.backtrace(board, word, i, j-1, k+1)
        ):
            return True
        board[i][j] = word[k]
        return False
```

#### [80. 删除有序数组中的重复项 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/)

##### 最简题解 [C++4行优美代码！](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/solution/c4xing-you-mei-dai-ma-by-xiaohu9527-ifr5/)

##### 最简代码

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums:
            if (i < 2) or (not(nums[i-1]==nums[i-2]==num)):
                nums[i] = num
                i += 1
        return i
```

#### [81. 搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)

##### 题解

```
1. 将数组等分成左右两部分，已知如果一部分无序，那么另一部分一定有序。
2. 只在有序的那部分寻找目标值，如果目标值在有序的那部分，那么舍弃无序那部分；反之舍弃有序的那部分。
3. 如果两部分都无法判断出无序，那就去掉数组最后一个值，继续判断。
```

##### 代码

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        i, j = 0, len(nums)-1
        while i < j:
            mid = i + (j-i) // 2
            if nums[mid+1] > nums[j]:  # 右边无序
                if nums[i] <= target <= nums[mid]:
                    j = mid
                else:
                    i = mid + 1
            elif nums[i] > nums[mid]: # 左边无序
                if nums[mid+1] <= target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid
            else:
                if nums[j] == target:
                    i = j
                else:
                    j -= 1
        return True if nums[i] == target else False
```

#### [82. 删除排序链表中的重复元素 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)

##### 题解

```
1. 节点个数 < 2时返回 head即可。

2. 前两个节点的值相等时，从第一个不等于该值的节点开始递归计算。

3. 前两个节点不等时，第一个节点后面 接上 递归计算的结果。
```

##### 代码

```python
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        
        if head.val == head.next.val:
            t = head.val
            while head and (head.val == t):
                head = head.next
            return self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
```

#### [83. 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)

##### 题解

```
用递归做，简简单单。
```

##### 代码

```python
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        
        p = self.deleteDuplicates(head.next)
        if head.val == p.val:
            return p
        else:
            head.next = p
            return head
```

#### [84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)

##### 最简题解：[找两边第一个小于它的值](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhao-liang-bian-di-yi-ge-xiao-yu-ta-de-zhi-by-powc/)

##### 最简代码

```python
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0] + heights + [0]
        rst, stack = 0, []
        for i in range(len(heights)):
            while stack and (heights[stack[-1]] > heights[i]):
                t = stack.pop(-1)
                rst = max(rst, heights[t] * (i - stack[-1] -1))
            stack.append(i)
        return rst
```

#### [85. 最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/)

##### 最简题解：[c++ python3 单调栈，一层一层的讨论。二维化一维， 调用84题的函数](https://leetcode-cn.com/problems/maximal-rectangle/solution/c-python3-dan-diao-zhan-yi-ceng-yi-ceng-haudm/)

##### 最简代码: 

```python
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        rst = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        for i in range(m):
            line = matrix[i]
            for j in range(n):
                if line[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            rst = max(rst, self.help(heights))
        return rst

    def help(self, heights):
        heights = [0] + heights + [0]
        stack = []
        rst = 0
        for i, num in enumerate(heights):
            while stack and heights[stack[-1]] > num:
                rst = max(rst, (i-stack[-2]-1) * heights[stack[-1]])
                stack.pop(-1)
            stack.append(i)
        return rst
```

#### [86. 分隔链表](https://leetcode-cn.com/problems/partition-list/)

##### 题解

```
待补充。
```

##### 代码

```python
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        q = self.partition(head.next, x)
        if head.val < x:
            head.next = q
            return head
        else:
            return self.insert(q, head, x)

    def insert(self, head, p, x):
        if not head:
            p.next = None
            return p
        if head.val < x:
            head.next = self.insert(head.next, p, x)
            return head
        else:
            p.next = head
            return p
```

#### [87. 扰乱字符串](https://leetcode-cn.com/problems/scramble-string/)

##### 题解

```
dp题解要用到三维的 dp数组 dp[len][i][j]，表示s1从i开始的len个字符跟 s2从j开始的len个字符够不够成扰乱字符串。
dp题解对我来说过于复杂，于是用了递归+lru_cache题解。
```

##### 代码

```python
from functools import lru_cache


class Solution(object):
    @lru_cache(None)
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        if n == 1:
            return True if s1 == s2 else False
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True 
        return False
```

#### [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)

##### 最简题解 [画解算法：88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/solution/hua-jie-suan-fa-88-he-bing-liang-ge-you-xu-shu-zu-/)

##### 最简代码

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        nums1[:n] = nums2[:n]
```

#### [89. 格雷编码](https://leetcode-cn.com/problems/gray-code/)

##### 题解

```
名为回溯题，实为公式题，一行代码即可解决~
```

##### 代码

```python
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i ^ (i >> 1) for i in range(pow(2, n))]
```

#### [90. 子集 II](https://leetcode-cn.com/problems/subsets-ii/)

##### 题解

```
回溯算法。
```

##### 代码

```python
from collections import Counter


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.rst = []
        self.backtrace([], Counter(nums))
        return self.rst
    
    def backtrace(self, trace, counts):
        self.rst.append(trace[:])
        for num in counts:
            if trace and (trace[-1] > num):
                continue
            if num in trace:
                continue
            for i in range(1, counts[num] + 1):
                trace.extend([num] * i)
                counts[num] -= i
                self.backtrace(trace, counts)
                for _ in range(i):
                    trace.pop(-1)
                counts[num] += i
```

#### [91. 解码方法](https://leetcode-cn.com/problems/decode-ways/)

##### 题解

```
一维dp数组。
dp[i] 表示以下标i结尾的字符串有几种题解。
```

##### 代码

```python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n
        for i in range(n):
            if i == 0:
                dp[0] = 0 if s == "0" else 1
            elif i == 1:
                if "10" <= s[i-1:i+1] <= "26":
                    dp[i] += 1
                if s[i-1] != "0" and s[i] != "0":
                    dp[i] += 1
            else:
                if "10" <= s[i-1:i+1] <= "26":
                    dp[i] += dp[i-2]
                if s[i] != "0":
                    dp[i] += dp[i-1]
            if not dp[i]:
                return 0
        return dp[-1]
```

#### [92. 反转链表 II](https://leetcode-cn.com/problems/reverse-linked-list-ii/)

##### 题解

```
递归求解。
```

##### 代码

```python
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == 1:
            return self.reverse_k(head, right)
        else:
            head.next = self.reverseBetween(head.next, left-1, right-1)
            return head
    
    def reverse_k(self, head, k):
        if k <= 1:
            return head
        rst = self.reverse_k(head.next, k-1)
        head.next.next, head.next = head, head.next.next
        return rst
```

#### [93. 复原 IP 地址](https://leetcode-cn.com/problems/restore-ip-addresses/)

##### 题解

```
每次试取前1个，前两个，前3个字符组成ip地址中的一小段。
```

##### 代码

```python
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not(4 <= len(s) <= 12):
            return []
        self.rst = []
        self.backtrace([], s)
        return self.rst
    
    def backtrace(self, trace, s):
        if not s:
            if len(trace) == 4:
                self.rst.append('.'.join(trace))
            return
        
        trace.append(s[:1])
        self.backtrace(trace, s[1:])
        trace.pop(-1)
        
        if int(s[:2]) >= 10:
            trace.append(s[:2])
            self.backtrace(trace, s[2:])
            trace.pop(-1)
        
        if 100 <= int(s[:3]) <= 255:
            trace.append(s[:3])
            self.backtrace(trace, s[3:])
            trace.pop(-1)
```

#### [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

##### 最简题解：[颜色标记法-一种通用且简明的树遍历方法](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/)

##### 最简代码:

```python
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, rst = [root], []
        while stack:
            x = stack.pop(-1)
            if isinstance(x, TreeNode):
                stack.extend([x.right, x.val, x.left])
            elif isinstance(x, int):
                rst.append(x)
        return rst
```

#### [95. 不同的二叉搜索树 II](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/)

##### 最简题解 [简单思路，C++递归](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/jian-dan-si-lu-cdi-gui-by-doctor_arknigh-2mjv/)

##### 最简代码

```python
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.res(1, n)
    
    def res(self, left, right):
        if left > right:
            return [None]
        elif left == right:
            return [TreeNode(left)]
        rst = []
        for i in range(left, right+1):
            left_nodes = self.res(left, i-1)
            right_nodes = self.res(i+1, right)
            for a in left_nodes:
                for b in right_nodes:
                    rst.append(TreeNode(i, a, b))
        return rst
```

#### [96. 不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees/)

##### 最简题解 [96. 不同的二叉搜索树，动态规划](https://leetcode-cn.com/problems/unique-binary-search-trees/solution/96-bu-tong-de-er-cha-sou-suo-shu-dong-ta-hiz1/)

##### 最简代码

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] + [0] * n
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]
```

#### [97. 交错字符串](https://leetcode-cn.com/problems/interleaving-string/)

##### 题解

```
还是偷懒用递归解了。。
```

##### 代码

```python
from functools import lru_cache


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        return self.inner(s1, s2, s3) or self.inner(s2, s1, s3)
    
    @lru_cache(None)
    def inner(self, s1, s2, s3):
        if not s1:
            return s2 == s3
        i = 0
        while i < len(s1) and s1[i] == s3[i]:
            if self.inner(s2, s1[i+1:], s3[i+1:]):
                return True
            i += 1
        return False
```

#### [98. 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)

##### 最简题解 [[前，中，后序三种遍历方式](https://leetcode-cn.com/problems/validate-binary-search-tree/solution/qian-zhong-hou-xu-san-chong-bian-li-fang-1kvx/)]

##### 最简代码

```python
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.last_val = float("-inf")
        return self.is_valid(root)
    
    def is_valid(self, root):
        if not root: 
            return True
        if not self.is_valid(root.left): 
            return False
        if root.val <= self.last_val: 
            return False
        self.last_val = root.val
        if not self.is_valid(root.right):
            return False
        return True
```

#### [100. 相同的树](https://leetcode-cn.com/problems/same-tree/)

##### 最简题解 [C++BFS小技巧只为更好看代码，DFS beats 100%代码](https://leetcode-cn.com/problems/same-tree/solution/cbfsxiao-ji-qiao-zhi-wei-geng-hao-kan-da-ziu8/)

##### 最简代码

```python
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p and q) is None:
            return True if (p or q) is None else False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

#### [101. 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/)

##### 最简题解 [对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode-solution/)

##### 最简代码

```
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.is_mirror(root.left, root.right)
    
    def is_mirror(self, r1, r2):
        if (r1 and r2) is None:
            return r1 is r2
        if r1.val != r2.val:
            return False
        return self.is_mirror(r1.left, r2.right) and self.is_mirror(r1.right, r2.left)
```

##### [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

##### 最简题解 [迭代+递归 多图演示 102.二叉树的层次遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/die-dai-di-gui-duo-tu-yan-shi-102er-cha-shu-de-cen/)

##### 最简代码

```python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rst = []
        queue = [(root,)]
        while queue:
            line = [ 
                node.val
                for nodes in queue
                for node in nodes
                if node
            ]
            if line:
                rst.append(line)
            queue = [
                (node.left, node.right)
                for nodes in queue
                for node in nodes
                if node
            ]
        return rst
```

#### [103. 二叉树的锯齿形层序遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)

##### 最简题解

##### 最简代码

```python
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rst, queue = [], [(root,)]
        while queue:
            line = [
                node.val
                for nodes in queue
                for node in nodes
                if node
            ]
            if line:
                rst.append(line)
            queue = [
                (node.left, node.right)
                for nodes in queue
                for node in nodes
                if node
            ]
        for i in range(len(rst)):
            if i % 2:
                rst[i] = rst[i][::-1]
        return rst
```

#### [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

##### 最简题解 [画解算法：104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/hua-jie-suan-fa-104-er-cha-shu-de-zui-da-shen-du-b/)

##### 最简代码 

```python
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

#### [105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

##### 最简题解 [动画演示 105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/dong-hua-yan-shi-105-cong-qian-xu-yu-zhong-xu-bian/)

##### 最简代码

```python
class Solution(object):
	def buildTree(self, preorder, inorder):
		if not (preorder and inorder):
			return None
		# 根据前序数组的第一个元素，就可以确定根节点	
		root = TreeNode(preorder[0])
		# 用preorder[0]去中序数组中查找对应的元素
		mid_idx = inorder.index(preorder[0])
		# 递归的处理前序数组的左边部分和中序数组的左边部分
		# 递归处理前序数组右边部分和中序数组右边部分
		root.left = self.buildTree(preorder[1:mid_idx+1],inorder[:mid_idx])
		root.right = self.buildTree(preorder[mid_idx+1:],inorder[mid_idx+1:])
		return root
```

#### [106. 从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

##### 最简题解 [动画演示 105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/dong-hua-yan-shi-105-cong-qian-xu-yu-zhong-xu-bian/)

##### 最简代码

```python
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:len(postorder)-1])
        return root
```

#### [107. 二叉树的层序遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)

##### 最简题解 

###### 最简代码

```python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rst = []
        queue = [(root,)]
        while queue:
            line = [ 
                node.val
                for nodes in queue
                for node in nodes
                if node
            ]
            if line:
                rst.append(line)
            queue = [
                (node.left, node.right)
                for nodes in queue
                for node in nodes
                if node
            ]
        return rst
```

#### [108. 将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)

##### 最简题解 [将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/jiang-you-xu-shu-zu-zhuan-huan-wei-er-cha-sou-s-33/)

##### 最简代码

```python
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return 0
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
```

#### [109. 有序链表转换二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/)

##### 题解

```
快慢指针不断找中点 slow，然后把链表分为 [left, slow) slow [slow.next, right) 三部分，递归构造树。
```

##### 代码

```python
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.res(head, None)

    def res(self, left, right):
        if left is right:
            return None
        
        slow = fast = left
        while (fast is not right) and (fast.next is not right):
            fast = fast.next.next
            slow = slow.next
        
        rst = TreeNode(slow.val)
        rst.left = self.res(left, slow)
        rst.right = self.res(slow.next, right)
        return rst
```

#### [110. 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)

##### 最简题解 [平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode-solution/)

##### 最简代码

```python
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.get_height(root.left) - self.get_height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def get_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))
```

#### [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)

##### 最简题解 [二叉树的最小深度-理解递归结束条件](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/li-jie-zhe-dao-ti-de-jie-shu-tiao-jian-by-user7208/)

##### 最简代码

```python
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```

#### [112. 路径总和](https://leetcode-cn.com/problems/path-sum/)

##### 最简题解 [路径总和](https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-by-leetcode-solution/)

##### 最简代码

```python
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left is root.right is None:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
```

#### [113. 路径总和 II](https://leetcode-cn.com/problems/path-sum-ii/)

##### 最简题解 [回溯算法（Java）](https://leetcode-cn.com/problems/path-sum-ii/solution/hui-su-suan-fa-shen-du-you-xian-bian-li-zhuang-tai/)

##### 最简代码

```python
class Solution(object):
    def pathSum(self, root, targetSum):
        self.rst = []
        self.backtrace([], root, targetSum)
        return self.rst
    
    def backtrace(self, trace, root, targetSum):
        if not root:
            return 
        if root.left is root.right is None:
            if root.val == targetSum:
                self.rst.append(trace + [root.val])
            return
        if root.left:
            trace.append(root.val)
            self.backtrace(trace, root.left, targetSum-root.val)
            trace.pop(-1)
        if root.right:
            trace.append(root.val)
            self.backtrace(trace, root.right, targetSum-root.val)
            trace.pop(-1)
```

#### [114. 二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)

##### 最简题解 [二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/)

##### 最简代码

```python
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.left, root.right = None, root.left
            root = root.right
```

#### [115. 不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/)

##### 题解

```
dp[i][j] 表示 s[:i] 中 包含 t[:j] 的序列个数.

这道题我自己想了一上午用极低的效率做了出来，看了大神的代码10分钟就能会了~
```

##### 代码

```python
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [ [0] * (n+1) for _ in range(m+1) ]
        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
```

#### [116. 填充每个节点的下一个右侧节点指针](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)

##### 最简题解 [116. 【递归】与【迭代】详解](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/116-di-gui-yu-die-dai-xiang-jie-by-carls-k8od/)

##### 最简代码

```python
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root or (not root.left):
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
```

#### [117. 填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)

##### 最简题解 [BFS解决（最好的击败了100%的用户）](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/bfsjie-jue-zui-hao-de-ji-bai-liao-100de-yong-hu-by/)

##### 最简代码

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        queue = [[root]]
        while queue:
            line = [
                node
                for nodes in queue
                for node in nodes
                if node
            ]
            for i in range(len(line)-1):
                line[i].next = line[i+1]
            queue = [
                [node.left, node.right]
                for nodes in queue
                for node in nodes
                if node
            ]
        return root
```

#### [118. 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle/)

##### 最简题解 [关于循环的一点反思](https://leetcode-cn.com/problems/pascals-triangle/solution/guan-yu-xun-huan-de-yi-dian-fan-si-by-fe-dlxw/)

##### 最简代码

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rst = []
        for n in range(1, numRows+1):
            line = [1] * n
            for j in range(1, n-1):
                line[j] = rst[-1][j] + rst[-1][j-1]
            rst.append(line)
        return rst
```

##### 最简题解 [119. 杨辉三角 II Python两种方法解题方便理解](https://leetcode-cn.com/problems/pascals-triangle-ii/solution/119-yang-hui-san-jiao-ii-pythonliang-cho-2ds0/)

##### 最简代码

```python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rst = [1] * (rowIndex+1)
        for n in range(1, rowIndex+2):
            for j in range(n-2, 0, -1):
                rst[j] = rst[j] + rst[j-1]
        return rst
```

#### [120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/)

##### 题解

```
dp[i][j] 表示以第i行，第j个顶点三角形的最小路径和。
```

##### 代码

```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[n][i] = triangle[-1][i-1]
        for i in range(n-1, 0, -1):
            for j in range(1, i+1):
                dp[i][j] = triangle[i-1][j-1] + min(dp[i+1][j], dp[i+1][j+1])
        return dp[1][1]
```

#### [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

##### 题解

```
参考 123 和 188，买卖股票问题有通用的套路。
dp[i][j][k] 表示第i天手上有j个股票(j∈{0, 1})且剩余k次交易机会时能获得的最大利润。
```

##### 代码

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[[0, 0], [0, 0]] for i in range(n+1)]
        
        dp[n][1][0] = prices[-1]
        for i in range(n-1, 0, -1):
            dp[i][0][0] = dp[i+1][0][0]
            dp[i][0][1] = max(dp[i+1][0][1], dp[i+1][1][0] - prices[i-1])
            dp[i][1][0] = max(dp[i+1][1][0], dp[i+1][0][0] + prices[i-1])
        return dp[1][0][1]
```

#### [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

##### 最简题解

```
只要今天价格比昨天高，就赚差价。
```

##### 最简代码

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        rst = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                rst += prices[i] - prices[i-1]
        return rst
```

#### [123. 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)

##### 题解

```
这道题是 [188, . , 买卖股票的最佳时机 IV] 中 k = 2 时的特例。
dp[i][j][k] 表示第i天手上有j个股票(j∈{0, 1})且剩余k次交易机会时能获得的最大利润。
```

##### 代码

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.res(prices, 2)
    
    def res(self, prices, max_k):
        n = len(prices)
        dp = []
        for i in range(n+1):
            dp.append([[0] * (max_k+1), [0] * (max_k+1)])
        
        for k in range(max_k):
            dp[n][1][k] = prices[-1]
        
        for i in range(n-1, 0, -1):
            for k in range(max_k+1):
                dp[i][0][k] = max(dp[i+1][0][k], (dp[i+1][1][k-1] - prices[i-1]) if k > 0 else 0)
                dp[i][1][k] = max(dp[i+1][1][k], dp[i+1][0][k] + prices[i-1])
#         pprint(dp)
        return dp[1][0][k]
```

#### [124. 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)

##### 最简题解 [124.递归的精髓，记录一下](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/124di-gui-de-jing-sui-ji-lu-yi-xia-by-821218213/)

##### 最简代码 

```python
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rst = float("-inf")
        self.bfs(root)
        return self.rst
    
    def bfs(self, root):
        if not root:
            return 0
        left = self.bfs(root.left)
        right = self.bfs(root.right)
        self.rst = max(self.rst, root.val + max(left, 0) + max(right, 0))
        return max(
            root.val,
            root.val+left,
            root.val+right,
        )
```

#### [125. 验证回文串](https://leetcode-cn.com/problems/valid-palindrome/)

##### 最简题解 [C++6行优美代码！！](https://leetcode-cn.com/problems/valid-palindrome/solution/c6xing-you-mei-dai-ma-by-xiaohu9527-507o/)

##### 最简代码

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [x.lower() for x in s if '0'<=x<='9' or 'a'<=x.lower()<='z']
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i+1, j-1
        return True
```

#### [126. 单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/)

##### 最简题解 [广度优先遍历建图 + 深度优先遍历找到所有解](https://leetcode-cn.com/problems/word-ladder-ii/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you--2/)

##### 最简代码

```python
from collections import defaultdict


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        wordList.add(beginWord)
        
        paterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                paterns[word[:i] + "*" + word[i+1:]].append(word)
        
        adj = defaultdict(list)
        for words in paterns.values():
            for i in range(len(words)):
                adj[words[i]].extend(words[:i] + words[i+1:])

        visited = set()
        queue = {beginWord}
        word2parents = defaultdict(list)
        while queue and (endWord not in queue):
            visited |= queue
            queue = {
                word2parents[new_word].append(word) or new_word
                for word in queue
                for new_word in adj[word]
                if new_word not in visited
            }
        self.rst = []
        self.backtrace([endWord], word2parents, beginWord)
        return self.rst
    
    def backtrace(self, trace, word2parents, beginWord):
        if trace[-1] == beginWord:
            self.rst.append(trace[::-1])
            return
        for parent in word2parents[trace[-1]]:
            trace.append(parent)
            self.backtrace(trace, word2parents, beginWord)
            trace.pop(-1)
```

#### [127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/)

##### 最简题解 [127. 单词接龙【为什么要用广搜】详解！](https://leetcode-cn.com/problems/word-ladder/solution/127-dan-ci-jie-long-wei-shi-yao-yao-yong-yan-sou-x/)

##### 最简代码

```python
from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        wordList.add(beginWord)
        
        paterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                paterns[word[:i] + "*" + word[i+1:]].append(word)
        
        adj = defaultdict(list)
        for words in paterns.values():
            for i in range(len(words)):
                adj[words[i]].extend(words[:i] + words[i+1:])

        wordList = set(wordList)
        visited = set()
        queue = {beginWord}
        rst = 1
        while queue:
#             print(queue)
            if endWord in queue:
                return rst
            visited |= queue
            queue = {
                new_word
                for word in queue
                for new_word in adj[word]
                if new_word not in visited
            }
            rst += 1
        return 0
```

#### [128. 最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence/)

##### 最简题解 [最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/)

##### 最简代码

```python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        nums = set(nums)
        for num in nums:
            if num-1 in nums:
                continue
            cur = num
            while cur in nums:
                cur += 1
            rst = max(rst, cur-num)
        return rst
```

#### [129. 求根节点到叶节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/)

##### 题解

##### 最简代码

```python
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rst = 0
        self.backtrace(0, root)
        return self.rst
    
    def backtrace(self, num, root):
        if not root:
            return
        if root.left is root.right is None:
            self.rst += num * 10 + root.val
        if root.left:
            self.backtrace(num * 10 + root.val, root.left)
        if root.right:
            self.backtrace(num * 10 + root.val, root.right)
```

#### [130. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)

##### 最简题解 [bfs+递归dfs+非递归dfs+并查集](https://leetcode-cn.com/problems/surrounded-regions/solution/bfsdi-gui-dfsfei-di-gui-dfsbing-cha-ji-by-ac_pipe/)

##### 最简代码

```python
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            self.bfs(board, i, 0)
            self.bfs(board, i, n-1)
        
        for j in range(n):
            self.bfs(board, 0, j)
            self.bfs(board, m-1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"
    
    def bfs(self, board, i, j):
        if (0 <= i < len(board)) and (0 <= j < len(board[0])) and (board[i][j] == "O"):
            board[i][j] = "A"
            self.bfs(board, i-1, j)
            self.bfs(board, i+1, j)
            self.bfs(board, i, j-1)
            self.bfs(board, i, j+1)
```

#### [131. 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning/)

##### 题解

```
看到分类既包含动态规划，又包含回溯，我还以为有多难。。

最基本的回溯算法就能解出来，效率还不低~
```

##### 代码

```python
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        self.rst = []
        self.backtrace([], s)
        return self.rst

    def backtrace(self, trace, s):
        if not s:
            self.rst.append(trace[:])
        for i in range(1, len(s)+1):
            word = s[:i]
            if word == word[::-1]:
                trace.append(word)
                self.backtrace(trace, s[i:])
                trace.pop(-1)
```

#### [134. 加油站](https://leetcode-cn.com/problems/gas-station/)

##### 最简题解 [134. 加油站:【贪心经典题目】详解](https://leetcode-cn.com/problems/gas-station/solution/134-jia-you-zhan-tan-xin-jing-dian-ti-mu-xiang-jie/)

##### 最简代码

```python
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        arr = [x-y for x, y in zip(gas, cost)]
        if sum(arr) < 0:
            return -1
        start = 0
        money = 0
        for i in range(len(arr)):
            money += arr[i]
            if money < 0:
                money = 0
                start = i+1
        return start
```

#### [135. 分发糖果](https://leetcode-cn.com/problems/candy/)

##### 最简题解 [分发糖果 （贪心思想，线性复杂度，清晰图解）](https://leetcode-cn.com/problems/candy/solution/)

##### 最简代码

```python
class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                left[i+1] += left[i]
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                right[i-1] += right[i]
        rst = 0
        for x, y in zip(left, right):
            rst += max(x, y)
        return rst
```

#### [136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number/)

##### 最简题解 [只出现一次的数字](https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/)

##### 最简代码

```python
class Solution(object):
    def singleNumber(self, nums):
        rst = 0
        for num in nums:
            rst ^= num
        return rst
```

#### [137. 只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii/)

##### 题解

```
把每个数字看成一个01串，比如把 [1, 1, 1, 2] 看成 [0001, 0001, 0001, 0010]，
然后统计每一位的"1"出现的个数.
0001
0001
0001
0010
----
0013

只保留1的个数不是3的倍数的位: 0013 -> 0010
把 0010 转换成10进制就是答案: 0010 -> 2
```

##### 代码

```python
class Solution(object):
    def singleNumber(self, nums):
        rst = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1 << i):
                    count += 1
            if count % 3 != 0:
                rst |= (1 << i)
				
        # 在Python里，如果答案是负数，需要进行如下转换，其它语言(Java, C++)应该不用.
        if rst & (1 << 31):
            return -((1 << 32)-1 - (rst-1))
        return rst
```

##### 二进制小知识

```
1. 负数的二进制表示，最高位是1； 正数的二进制表示，最高位是0
2. 负数的补码等于其反码+1
```

##### 推广

```
把 上述代码中的 `if count % 3 != 0:` 这一行中的3换成 k，就能解决"除一个数字出现1次，其余数字出现k次的问题."
```

#### [138. 复制带随机指针的链表](https://leetcode-cn.com/problems/copy-list-with-random-pointer/)

##### 最简题解

```
建立旧节点到新节点的映射。
```

##### 最简代码

```python
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        d = {None: None}
        p = head
        while p:
            d[p] = Node(p.val)
            p = p.next
        
        p = head
        while p:
            d[p].next = d[p.next]
            d[p].random = d[p.random]
            p = p.next
        
        return d[head]
```

#### [139. 单词拆分](https://leetcode-cn.com/problems/word-break/)

##### 题解

```
dp[i] 表示 s[:i] 能否用 wordDict 拆分。
```

##### 代码

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for word in wordDict:
                if s[i-len(word):i] == word and dp[i-len(word)]:
                    dp[i] = True
                    break
        return dp[-1]
```

#### [140. 单词拆分 II](https://leetcode-cn.com/problems/word-break-ii/)

##### 题解

```
是测试用例改过了么？为啥我直接暴力就执行用书超过 89%了(20ms).
```

##### 代码

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.rst = []
        self.backtrace([], s, wordDict)
        return self.rst
    
    def backtrace(self, trace, s, wordDict):
        if not s:
            self.rst.append(" ".join(trace))
            return
        for word in wordDict:
            if s[:len(word)] == word:
                trace.append(word)
                self.backtrace(trace, s[len(word):], wordDict)
                trace.pop(-1)
```

##### [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)

##### 题解

```
用两个指针指向链表开头
然后不断循环：一个指针向后走一步，另一个指针向后走两步
如果：
	走的快的指针走到了链表结尾: 那就是没有环
	快慢指针相遇: 那就是有环
```

##### 代码

```python
class Solution(object):
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False
```

#### [142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

##### 题解

```
快慢指针相遇后，新建一个指针指向链表头。
然后循环：新指针向后走一步，慢指针向后走一步
新指针和慢指针相遇的点，就是环的入口。
```

##### 代码

```python
class Solution(object):
    def detectCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                p = head
                while p is not slow:
                    p = p.next
                    slow = slow.next
                return p
        return None
```

#### [143. 重排链表](https://leetcode-cn.com/problems/reorder-list/)

##### 题解

```
1. 把链表一分为二，第一段从开头到中间，第二段从中间到结尾。
2. 把第二段链表逆置。
3. 把两段链表交替连接起来。
```

##### 细节

```
快慢指针找链表的中点，作为第二段链表的开头head2。
递归逆置链表是之前必须要掌握（背过）的。
```

##### 代码

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not (head and head.next and head.next.next):  # 小于3个节点
            return head
        
        slow = fast = head
        fast = fast.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        h1, h2 = head, slow.next
        slow.next = None
        
        h2 = self.reverse(h2)
        return self.combine(h1, h2)
    
    def combine(self, h1, h2):
        if (h1 and h2) is None:
            return h1 or h2
        
        h1.next, h2.next = h2, self.combine(h1.next, h2.next)
        return h1
    
    def reverse(self, head):
        if not (head and head.next):
            return head
        
        rst = self.reverse(head.next)
        head.next.next = head
        head.next = None
        
        return rst
```

#### [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)

##### 最简题解：[颜色标记法-一种通用且简明的树遍历方法](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/)

##### 最简代码

```python
class Solution(object):
    def preorderTraversal(self, root):
        rst = []
        stack = [root]
        while stack:
            cur = stack.pop(-1)
            if isinstance(cur, TreeNode):
                stack.extend([cur.right, cur.left, cur.val])
            elif isinstance(cur, int):
                rst.append(cur)
        return rst
```

#### [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)

##### 最简题解：[颜色标记法-一种通用且简明的树遍历方法](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/)

##### 最简代码

```python
class Solution(object):
    def postorderTraversal(self, root):
        rst = []
        stack = [root]
        while stack:
            cur = stack.pop(-1)
            if isinstance(cur, TreeNode):
                stack.extend([cur.val, cur.right, cur.left])
            elif isinstance(cur, int):
                rst.append(cur)
        return rst
```

##### 推广

```
改变代码 中 [cur.right, cur.left, cur.val] 的顺序，可以实现中序和后续遍历。

前序是:     [cur.right, cur.left, cur.val]  
中序是:     [cur.right, cur.val, cur.left]
后序是:     [cur.val, cur.right, cur.left]

其实这个顺序就是 x序的[逆]序。
如中序本来是 左根右 ->(逆序一下)-> 右根左 -> [cur.right, cur.val, cur.left]
前序和后续同理。
```

#### [146. LRU 缓存机制](https://leetcode-cn.com/problems/lru-cache/)

##### 最简题解

```
需要一个双链表和一个字典。

双链表的每个结点存四个数据：
	1）key
	2) val
	3) pre  前一个节点
	4) next 后一个节点
双链表需要实现两个方法：1）删除指定节点 2）在某一节点后插入一个结点
双链表构建时，头尾各有一个辅助节点

字典内容是 key2node

put和get操作结束前，只要key在字典中，就把该key对应的节点放在链表头
```

##### 最简代码

```python
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.pre = None


class LRUCache(object):

    def __init__(self, capacity):
        self.th = Node(None, None)  # 辅助头
        self.tt = Node(None, None)  # 辅助尾
        self.th.next = self.tt
        self.tt.pre = self.th
        self.key2node = {}
        self.n = capacity
	
  	def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def insert_after(self, before, node):
        after = before.next
        before.next = node
        after.pre = node
        node.next = after
        node.pre = before
        
    def get(self, key):
        if key in self.key2node:
            node = self.key2node[key]
            self.remove(node)
            self.insert_after(self.th, node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
            self.remove(node)
            self.insert_after(self.th, node)
        else:
            if len(self.key2node) == self.n:
                self.key2node.pop(self.tt.pre.key)
                self.remove(self.tt.pre)
            node = Node(key, value)
            self.key2node[key] = node
            self.insert_after(self.th, node)
```

##### 注意

```
在lru增删数据时，先改字典，再改链表能减少出错。
```

#### [147. 对链表进行插入排序](https://leetcode-cn.com/problems/insertion-sort-list/)

##### 最简题解 [147. 对链表进行插入排序【原地修改，清晰讲解】](https://leetcode-cn.com/problems/insertion-sort-list/solution/147-dui-lian-biao-jin-xing-cha-ru-pai-xu-248j/)

##### 最简代码

```python
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rst = ListNode()
        cur = head
        while cur:
            p = rst
            while p.next and p.next.val <= cur.val:
                p = p.next
            p.next, cur.next, cur = cur, p.next, cur.next
        return rst.next
```

#### [148. 排序链表](https://leetcode-cn.com/problems/sort-list/)

##### 最简题解 [Sort List （归并排序链表）](https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/)

就是实现归并排序。

##### 最简题解

```python
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None):
            return head
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        h1, h2, slow.next = head, slow.next, None
        h1 = self.sortList(h1)
        h2 = self.sortList(h2)
        return self.merge(h1, h2)
    
    def merge(self, h1, h2):
        if (h1 and h2) is None:
            return h1 or h2
        if h1.val < h2.val:
            h1.next = self.merge(h1.next, h2)
            return h1
        else:
            h2.next = self.merge(h1, h2.next)
            return h2
```

#### [150. 逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)

##### 最简题解

```
遍历每一个元素：
    1. 是数字就入栈
    2. 是加减乘除就拿出两个栈顶元素，做相应运算后其结果入栈
做完上述操作，栈中只会剩下一个元素，就是答案
```

##### 最简代码

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        d = {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: int(a/b),
        }
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b, a = stack.pop(-1), stack.pop(-1)
                stack.append(d[token](a, b))
            else:
                stack.append(int(token))
        return stack[0]
```

##### 注意 Python3 和 Python 的除法

```
python3: int(b / a)
python: int(b / float(a))
```

#### [151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

##### 最简题解

##### 最简代码

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])
```

#### [152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/)

##### 题解

```
big[i] 以 nums[i-1] 结尾的【最大】子数组乘积。
small[i] 以 nums[i-1] 结尾的【最小】子数组乘积。

big[i] 取以下三者中的最大值:
    1. nums[i-1]
    2. nums[i-1] * big[i-1]
    3. nums[i-1] * small[i-1]
   
small[i] 则取上述三者的最小值
```

##### 代码

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        big, small = [0] * (n+1), [0] * (n+1)
        big[0], small[0] = 1, 1
        for i in range(1, n+1):
            big[i] = max(nums[i-1], nums[i-1] * big[i-1], nums[i-1] * small[i-1])
            small[i] = min(nums[i-1], nums[i-1] * big[i-1], nums[i-1] * small[i-1])
        return max(big[1:])
```

##### 参考 [ 多种思路求解](https://leetcode-cn.com/problems/maximum-product-subarray/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/)

#### [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

##### 题解

```
这样不是最简的，但比较容易想：

把数组等分成左右两段
1. 如果一段有序，一段无序，那最小值一定在无序的那段里。
2. 如果两段都有序，那第一个元素就是最小值。
```

##### 代码

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i < j:
            mid = i + (j-i)//2
            if nums[i] > nums[mid]:
                j = mid
            elif nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = i
        return nums[i]
```

#### [154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

##### 题解

```
这道题很好理解，用非常简单的思路就能python 4ms超过100%。

1. 把数组等分成左右两段
2. 如果一段有序另一段无序，那最小值一定在无序的那段里
3. 如果两段都有序，就比较数组两头的值，去掉值较大的那一头
```

##### 代码

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i < j:
            mid = i + (j-i)//2
            if nums[i] > nums[mid]:
                j = mid
            elif nums[mid] > nums[j]:
                i = mid + 1
            else:
                if nums[i] < nums[j]:
                    j -= 1
                else:
                    i += 1
        return nums[i]
```

##### 参考: [寻找旋转排序数组中的最小值 II（二分法，极简，图解](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/154-find-minimum-in-rotated-sorted-array-ii-by-jyd/)

#### [155. 最小栈](https://leetcode-cn.com/problems/min-stack/)

##### 最简题解 [最小栈 （辅助栈法，清晰图解）](https://leetcode-cn.com/problems/min-stack/solution/min-stack-fu-zhu-stackfa-by-jin407891080/)

##### 最简代码

```python
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        self.min_stack.append(min(
            x,
            self.min_stack[-1] if self.min_stack else float('inf'),
        ))

    def pop(self):
        self.stack.pop(-1)
        self.min_stack.pop(-1)

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
```

#### [160. 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)

##### 题解

```
两个指针分别指向两个链表头,
然后一起向后移动，如果某个指针走到了末尾，就把这个指针重新指向另一个链表头，
重复上述过程，直到两个指针重叠，则重叠的节点就是答案。
```

##### 代码

```python
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p1, p2 = headA, headB
        while p1 is not p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
```

#### [162. 寻找峰值](https://leetcode-cn.com/problems/find-peak-element/)

##### 题解

```
1. 将数组等分成左右两段。
2. 比较两段的接缝处，即比较第一段的最后一个元素的值和第二段第一个元素的值，保留大的值所在的段。
```

##### 代码

```python
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i < j:
            mid = i + (j-i)//2
            if nums[mid] < nums[mid+1]:
                i = mid + 1
            else:
                j = mid
        return i
```

#### [164. 最大间距](https://leetcode-cn.com/problems/maximum-gap/)

##### 最简题解 [[Python3] 桶排序](https://leetcode-cn.com/problems/maximum-gap/solution/python3-tong-pai-xu-by-yanghk/)

##### 代码

```python
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        max_, min_ = max(nums), min(nums)
        b_len = max(1, (max_ - min_) // len(nums))
        b_size = max_ // b_len + 1
        buckets = [[] for _ in range(b_size)]
        for num in nums:
            buckets[(num-min_)//b_len].append(num)
        rst = 0
        left = None
        for bucket in buckets:
            if not bucket:
                continue
            if left is None:
                left = max(bucket)
            else:
                rst = max(rst, min(bucket)-left)
                left = max(bucket)
        return rst
```

#### [165. 比较版本号](https://leetcode-cn.com/problems/compare-version-numbers/)

##### 最简题解 [比较版本号](https://leetcode-cn.com/problems/compare-version-numbers/solution/bi-jiao-ban-ben-hao-by-leetcode/)

##### 最简代码

```python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(y) for y in version2.split('.')]
        n = max(len(v1), len(v2))
        for i in range(n):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0 
```

#### [166. 分数到小数](https://leetcode-cn.com/problems/fraction-to-recurring-decimal/)

##### 题解

```
在不断进行除法的过程中，被除数是一直在变化的，除数是固定的。
当被除数是0时，说明能整除，直接返回结果即可。
记录小数部分每个被除数及其对应的当时结果字符串的长度，
当某个被除数出现次数大于1时，在结果字符串加入括号并返回。
```

##### 代码

```python
cclass Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        d = {}
        rst = "-" if numerator * denominator < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)
        while numerator:
            if numerator < denominator:
                numerator *= 10
                if not d:  # 第一次到小数点后
                    rst += "0." if rst in ["-", ""] else "."
                if numerator in d:  # 该被除数在小数部分出现过
                    i = d[numerator]
                    rst = rst[:i] + "(" + rst[i:] + ")"
                    break
                d[numerator] = len(rst)
            rst += str(numerator // denominator)
            numerator = numerator % denominator
        return rst or "0"
```

#### [167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

##### 题解

```
1. 左右两个指针分别指向数组的两端。
2. 两个指针代表的数相加，小于目标值则左指针向右；大于目标值则右指针向左，等于目标值则返回。
```

##### 代码

```python            
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers)-1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return[i+1, j+1]
```

#### [168. Excel表列名称](https://leetcode-cn.com/problems/excel-sheet-column-title/)

##### 题解

```
本质是10进制转26进制
把 1->A，2->B 换成0->A，1->B来算，就好想多了。
```

##### 代码

```python
class Solution(object):
    def convertToTitle(self, n):
        rst = ""
        while n:
            n -= 1
            rst = chr(65 + n % 26) + rst
            n //= 26
        return rst
```

#### [169. 多数元素](https://leetcode-cn.com/problems/majority-element/)

##### 最简题解 [摩尔投票法](https://leetcode-cn.com/problems/majority-element/solution/mo-er-tou-piao-fa-by-wo-yao-chu-qu-luan-tn5kg/)

##### 最简代码

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst, count = None, 0
        for num in nums:
            if rst == num:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 1
                    rst = num
        return rst
```

#### [171. Excel表列序号](https://leetcode-cn.com/problems/excel-sheet-column-number/)

##### 题解

```
相当于26进制。
```

##### 代码

```python
class Solution(object):
    def titleToNumber(self, s):
        rst = 0
        for letter in s:
            rst *= 26
            rst += ord(letter) -65 + 1
        return rst
```

#### [172. 阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes/)

##### 题解

```
要知道n!结尾有几个0，相当于要知道 n! 能分解成几个 2x5。
因为 2 出现次数比5多，所以就要知道 n! 质因数分解结果里 有几个5。
规律是: 
    1. 每5个数字出现一个5，如 5, 10, 15
    2. 每25个数字出现两个5，如 25, 50, 75
    3. 每125个数字出现3个，如 125，250
```

##### 代码

```python
class Solution(object):
    def trailingZeroes(self, n):
        rst = 0
        while n:
            rst += n // 5
            n = n // 5
        return rst
```

参考: [Q172. Factorial Trailing Zeroes](https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/q172-factorial-trailing-zeroes-by-ronhou/)


#### [173. 二叉搜索树迭代器](https://leetcode-cn.com/problems/binary-search-tree-iterator/)

##### 最简题解

```
直接把中序遍历的结果存到数组里，再依次输出。
```

##### 最简代码

```python
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.vals = []
        self.i = 0
        
        stack = [root]
        while stack:
            x = stack.pop(-1)
            if x is None:
                continue
            if isinstance(x, int):
                self.vals.append(x)
            else:
                stack.extend([x.right, x.val, x.left])

    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        return self.vals[self.i-1]


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.vals)
```

#### [174. 地下城游戏](https://leetcode-cn.com/problems/dungeon-game/submissions/)

##### 题解

```
这是我蒙出来的，不好写题解。。
```

##### 代码

```python
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[1] * n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                maybe = []
                if i != m-1:
                    maybe.append(dp[i+1][j]-dungeon[i+1][j])
                if j != n-1:
                    maybe.append(dp[i][j+1]-dungeon[i][j+1])
                dp[i][j] = max(min(maybe) if maybe else 0, 1)
        return max(dp[0][0] - dungeon[0][0], 1)
```

#### [179. 最大数](https://leetcode-cn.com/problems/largest-number/)

##### 最简题解 [最大数](https://leetcode-cn.com/problems/largest-number/solution/zui-da-shu-by-leetcode/)

##### 最简代码

```python
from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(lambda x, y: -1 if x+y > y+x else 1))
        
        return "".join(nums).lstrip("0") or "0"
```

#### [187. 重复的DNA序列](https://leetcode-cn.com/problems/repeated-dna-sequences/)

##### 最简题解

```
用字典记录下所有长度为10的子串出现的次数。
```

##### 最简代码

```python
from collections import defaultdict


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        d = defaultdict(int)
        for i in range(len(s)-9):
            d[s[i:i+10]] += 1
        return list([k for k, v in d.items() if v > 1])
```

#### [188. 买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)

##### 题解

```
dp[i][j][k] 表示第i天手上有j个股票(j∈{0, 1})且剩余k次交易机会时能获得的最大利润。
```

##### 代码

```python
class Solution(object):
    def maxProfit(self, max_k, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = []
        for i in range(n+1):
            dp.append([[0] * (max_k+1), [0] * (max_k+1)])
        
        for k in range(max_k):
            dp[n][1][k] = prices[-1]
        
        for i in range(n-1, 0, -1):
            for k in range(max_k+1):
                dp[i][0][k] = max(dp[i+1][0][k], (dp[i+1][1][k-1] - prices[i-1]) if k > 0 else 0)
                dp[i][1][k] = max(dp[i+1][1][k], dp[i+1][0][k] + prices[i-1])
        return dp[1][0][k]
```

#### [旋转数组](https://leetcode-cn.com/problems/rotate-array/)

##### 题解

```
先将数组分成两部分，右边有k个元素，左边有n-k的元素。
然后分别将两个数组逆序，再把两个数组拼起来整体逆序，得到的就是答案。
```

##### 代码

```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-1-k)
        self.reverse(nums, 0, n-1)
    
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
```

#### [189. 旋转数组](https://leetcode-cn.com/problems/rotate-array/)

##### 最简题解 [Python3, 三种思路，189](https://leetcode-cn.com/problems/rotate-array/solution/python3-san-chong-si-lu-189-by-lionking8-arbt/)

##### 最简代码

```python
class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
```

#### [190. 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/)

##### 最简题解

```
每次取个位数字，连取32次。
```

##### 最简代码

```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rst = 0
        for _ in range(32):
            rst = (rst << 1) | (n & 1)
#             print(rst)
            n = n >> 1
        return rst
```

#### [191. 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits/)

##### 最简题解

```
判断个位数是不是1，重复很多次。
```

##### 最简代码

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = 0
        while n:
            rst += n & 1
            n >>= 1
        return rst
```

#### [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)

##### 题解

```
dp[i] 表示打劫 nums[:i+1] 最多能得多少钱。
```

##### 代码

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]
```

#### [199. 二叉树的右视图](https://leetcode-cn.com/problems/binary-tree-right-side-view/)

##### 题解

```
借助队列分层遍历二叉树，每次加入最后一个节点的值。
```

##### 代码

```python
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rst = []
        queue = [(root,)]
        while queue:
            rst.extend([
                node.val
                for nodes in queue
                for node in nodes
                if node
            ][-1:])
            queue = [
                (node.left, node.right)
                for nodes in queue
                for node in nodes
                if node
            ]

        return rst
```

#### [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

##### [200. 岛屿数量（DFS / BFS）](https://leetcode-cn.com/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/)

```
广度搜索。
```

##### 最简代码

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rst = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    rst += 1
                    self.bfs(grid, i, j, rst)
        return rst
    
    def bfs(self, grid, i, j, x):
        if (0<=i<len(grid)) and (0<=j<len(grid[0])) and (grid[i][j] == "1"):
            grid[i][j] = x
            self.bfs(grid, i+1, j, x)
            self.bfs(grid, i-1, j, x)
            self.bfs(grid, i, j+1, x)
            self.bfs(grid, i, j-1, x)
```
