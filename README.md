# Leetcode
简明力扣题解：用最简单的思路或最简洁的代码。

#### [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

##### 解法

```
将所有的数两两比较，找到符合条件的两个数就返回下标。
```

##### 代码

```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

#### [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

##### 解法

```
递归求解
```

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

##### 解法

```
遍历每个字符：
	要是这个字符没在队列中，就在队列中加入这个字符。
  要是这个字符在队列中，就在队列里把这个字符之前的部分都砍掉
在这个过程中，队列的最大长度就是答案。
```

##### 代码

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        rst = 0
        queue = []
        for letter in s:
            while letter in queue:
                queue.pop(0)
            queue.append(letter)
            rst = max(rst, len(queue))
        return rst
```

#### [4. 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

##### 解法

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

##### 参考：[综合百家题解，总结最清晰易懂的二分解法！](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/zong-he-bai-jia-ti-jie-zong-jie-zui-qing-xi-yi-don/)

#### [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

##### 解法

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

#### [134. 加油站](https://leetcode-cn.com/problems/gas-station/)

##### 解法

```
有一个环形路上有n个站点； 每个站点都有一个好人或一个坏人；
好人会给你钱，坏人会收你一定的过路费，如果你带的钱不够付过路费，坏人会跳起来把你砍死； 
问：从哪个站点出发，能绕一圈活着回到出发点?

首先考虑一种情况：如果全部好人给你 的钱加起来 小于 坏人收的过路费之和，
那么总有一次你的钱不够付过路费，
你的结局注定会被砍死。

假如你随机选一点 start 出发，那么你肯定会选一个有好人的站点开始，因为开始的时候你没有钱，遇到坏人只能被砍死；

现在你在start出发，走到了某个站点end，被end站点的坏人砍死了，
说明你在 [start, end) 存的钱不够付 end点坏人的过路费，
又因为start站点是个好人，所以在 (start, end) 里任何一点出发，你存的钱会比现在还少，还是会被end站点的坏人砍死；

于是你重新读档，聪明的选择从 end+1点出发，继续你悲壮的征程；
终于有一天，你发现自己走到了尽头（下标是n-1)的站点而没有被砍死；
此时你犹豫了一下，那我继续往前走，身上的钱够不够你继续走到出发点Start?

当然可以，因为开始已经判断过，好人给你的钱数是大于等于坏人要的过路费的，
你现在攒的钱完全可以应付 [0, start) 这一段坏人向你收的过路费。 
这时候你的嘴角微微上扬，眼眶微微湿润，因为你已经知道这个世界的终极奥秘：Start就是这个问题的答案。
```

##### 代码

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

##### 解法

```
1. 先给每个同学发一块糖。
2. 从左向右：如果右边的同学分数比你高，你就把手上的糖都给右边的同学。
3. 把糖收回，重新发给每个同学一块糖。
4. 从右向左：如果左边的同学分数比你高，你就把手上的糖都给左边的同学。
5. 每个同学都记得自己手上最多有过几块糖，把这些数加起来就是答案。
```

##### 代码

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

##### 解法

```
数组中所有数字做异或操作，最终得到一个数就是答案
```

##### 代码

```python
class Solution(object):
    def singleNumber(self, nums):
        rst = 0
        for num in nums:
            rst ^= num
        return rst
```

#### [137. 只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii/)

##### 解法

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

##### 解法

```
从链表头遍历到链表尾，用一个字典记录旧节点和生成的新节点的对应关系，设置好新节点的value。
再遍历一遍旧链表，把每个新节点的next 和 random指针的位置设置好。
```

##### 代码

```python
class Solution(object):
    def copyRandomList(self, head):
        old2new = {None: None}
        cur = head
        while cur:
            old2new[cur] = Node(cur.val)
            cur = cur.next

        old = head
        while old:
            old2new[old].next = old2new[old.next]
            old2new[old].random = old2new[old.random]
            old = old.next

        return old2new[head]
```

#### [139. 单词拆分](https://leetcode-cn.com/problems/word-break/)

##### 解法

```
因为Python3自带备忘录，所以写动态规划有无可比拟的巨大优势（优势指写完代码的用时，不是指代码的运行时间）
直接写完递归，再加个备忘录(lru_cache)就可以了。
```

##### 代码

```python
from functools import lru_cache


class Solution(object):
    def wordBreak(self, s, wordDict):
        self.words = wordDict
        return self.res(s)

    @lru_cache(None)
    def res(self, s):
        if not s:
            return True
        for word in self.words:
            if s.startswith(word):
                if self.res(s[len(word):]):
                    return True
        return False
```

#### [140. 单词拆分 II](https://leetcode-cn.com/problems/word-break-ii/)

##### 解法

```
用普通的回溯法，再结合题目139的单词拆分先判断true和false就行了。
```

##### 代码

```python
from functools import lru_cache


class Solution(object):
    def wordBreak(self, s, wordDict):
        self.words = wordDict
        self.rst = []
        self.backtrace(s, [])
        return self.rst

    def backtrace(self, s, trace):
        if not s:
            self.rst.append(" ".join(trace))
            return
        for word in self.words:
            if s.startswith(word) and self.is_valid(s[len(word):]):
                trace.append(word)
                self.backtrace(s[len(word):], trace)
                trace.pop(-1)

    @lru_cache(None)
    def is_valid(self, s):
        if not s:
            return True
        for word in self.words:
            if s.startswith(word):
                if self.is_valid(s[len(word):]):
                    return True
        return False
```

##### [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)

##### 解法

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

##### 解法

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

##### 解法

```
1. 把链表一分为二，第一段从开头到中间，第二段从中间到结尾，要保证第一段的长度>=第二段的长度。
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
class Solution(object):
    def reorderList(self, head):
        if not head:
            return
        # 寻找第二段链表头
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None

        # 第二段链表逆置
        head2 = self.reverse(head2)

        # 合并
        self.combine(head, head2)

    def reverse(self, head):
        if (not head) or (not head.next):
            return head
        rst = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return rst

    def combine(self, head1, head2):
        if not head2:
            return head1

        t = self.combine(head1.next, head2.next)
        head1.next = head2
        head2.next = t
        return head1
```

#### [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)

##### 解法

```
用栈做辅助。
检查栈顶元素，是数字就`输出`，是节点就按一定顺序把该节点的左右孩子和节点值入栈。
```

##### 代码

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

##### 推广

```
改变代码 中 [cur.right, cur.left, cur.val] 的顺序，可以实现中序和后续遍历。

本题前序是: [cur.right, cur.left, cur.val]  
中序是:     [cur.right, cur.val, cur.left]
后序是:     [cur.val, cur.right, cur.left]

其实这个顺序就是 x序的[逆]序。
如中序本来是 左根右 ->(逆序一下)-> 右根左 -> [cur.right, cur.val, cur.left]
前序和后续同理。
```

#### [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)

##### 解法

```
套模板
```

##### 代码

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

##### 解法

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

##### 代码

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

##### 解法

###### 1. 在 节点p1 后面插入 节点 p2

```python
p2.next = p1.next
p1.next = p2
```

###### 2. 在有序链表中插入p2，找到p2要插入在哪个节点后面

```python
p1 = th  # th 是指向已排序链表头的虚拟节点
while p1.next and p1.next.val < p2.val:
    p1 = p1.next
```

###### 3. 在有序链表中插入p2

```python
p1 = th  # th 是指向已排序链表头的虚拟节点
while p1.next and p1.next.val < p2.val:
    p1 = p1.next

p2.next = p1.next
p1.next = p2
```

###### 4. 在有序链表中依次插入另一个链表(head2)的每个节点

```python
p2 = head2
while p2:
    p2_next = p2.next
    
    p1 = th  # th 是指向已排序链表头的虚拟节点
    while p1.next and p1.next.val < p2.val:
        p1 = p1.next
    p2.next = p1.next
		p1.next = p2

    p2 = p2_next
```

###### 5. 最终

```Python
class Solution(object):
    def insertionSortList(self, head):
        th = ListNode(0)

        p2 = head
        while p2:
            p2_next = p2.next

            p1 = th
            while p1.next and p1.next.val < p2.val:
                p1 = p1.next
            p2.next = p1.next
            p1.next = p2

            p2 = p2_next

        return th.next
```

#### [148. 排序链表](https://leetcode-cn.com/problems/sort-list/)

##### 解法

就是实现归并排序。

###### 1. 尾插法合并两个有序链表

```python
th = tail = ListNode(0)
while h1 and h2:
    if h1.val < h2.val:
        tail.next = h1
        h1 = h1.next
        tail = tail.next
    else:
        tail.next = h2
        h2 = h2.next
        tail = tail.next
tail.next = h1 or h2

return th.next
```

###### 2. 找到链表中点，将链表1分为2

```python
h1 = fast = slow = head
while fast.next and fast.next.next:
    fast = fast.next.next
    slow = slow.next
h2 = slow.next
slow.next = None
```

###### 3. 最终

```python
class Solution(object):
    def sortList(self, head):
        # 只有0个或1个节点就不用排序
        if (head is None) or (head.next is None):
            return head
        
        # 将链表1分为2
        h1 = fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        h2 = slow.next
        slow.next = None
				
        # 将前后两段链表分别排序
        h1 = self.sortList(h1)
        h2 = self.sortList(h2)
				
        # 合并两个有序链表
        th = tail = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
                h1 = h1.next
                tail = tail.next
            else:
                tail.next = h2
                h2 = h2.next
                tail = tail.next
        tail.next = h1 or h2

        return th.next
```

#### [149. 直线上最多的点数](https://leetcode-cn.com/problems/max-points-on-a-line/)

##### 代码

```Python
from collections import defaultdict
from fractions import Fraction


class Solution:
    def maxPoints(self, points):
        if not points:
            return 0
        rst = 0
        for i in range(len(points)):
            same = 0
            rake2num = defaultdict(int)
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    same += 1
                elif points[i][0] == points[j][0]:
                    rake2num[None] += 1
                else:
                    # 想不到吧？？Python有自带的分数库
                    rake = Fraction(points[i][1] - points[j][1]) / Fraction(points[i][0] - points[j][0])
                    rake2num[rake] += 1
            max_ = same + 1
            if rake2num:
                max_ += max(rake2num.values())
            rst = max(rst, max_)
        return rst
```

#### [150. 逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)

##### 解法

```
遍历每一个元素：
    1. 是数字就入栈
    2. 是加减乘除就拿出两个栈顶元素，做相应运算后其结果入栈
做完上述操作，栈中只会剩下一个元素，就是答案
```

##### 代码

```python
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
                continue

            num2 = stack.pop(-1)
            num1 = stack.pop(-1)
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                stack.append(int(num1 / num2))
        return stack[0]
```

##### 注意 Python3 和 Python 的除法

```
python3: int(b / a)
python: int(b / float(a))
```

#### [151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

##### 解法

```
1. 去除多余空格
2. 将整个字符串逆序
3. 将每个单词逆序
```

##### 代码

```python
class Solution(object):
    def reverseWords(self, s):
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
```

#### [152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/)

##### 解法

```
1. 如果数组里没有0:
	1.1 如果负数的个数是偶数，那么所有数相乘最大
	1.2 如果负数的个数是奇数，那么要么 前n-1个数相乘最大，要么后n-1个数相乘最大
```

##### 代码

```python
class Solution(object):
    def maxProduct(self, nums):
        nums2 = nums[::-1]  # nums 的逆序
        for i in range(1, len(nums)):
            nums[i] = (nums[i-1] or 1) * nums[i]
            nums2[i] = (nums2[i-1] or 1) * nums2[i]
        return max(nums + nums2)
```

##### 参考 [ 多种思路求解](https://leetcode-cn.com/problems/maximum-product-subarray/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/)

#### [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

##### 解法

```
给一个数组，一刀将它等分成左右两段。
如果右段有序，就抛弃右段，否则就抛弃左段。
当数组中只有一个数的时候停止。
```

##### 代码

```python
class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
```

#### [154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

##### 解法

```
还是把数组1分为2：
  1. 右边严格有序就抛弃右边
  2. 右边无序就抛弃左边
  3. 否则就 right = right - 1
```

##### 代码

```python
class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]
```

##### 参考: [寻找旋转排序数组中的最小值 II（二分法，极简，图解](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/154-find-minimum-in-rotated-sorted-array-ii-by-jyd/)

#### [155. 最小栈](https://leetcode-cn.com/problems/min-stack/)

##### 解法

```
需要一个正常栈和一个辅助栈。
出栈时，两个栈都正常出栈操作。
入栈时，正常栈正常入栈，辅助栈将要入栈的元素和辅助栈顶元素做比较，选小的入栈。
根据以上规矩，辅助栈顶永远是最小的元素。
```

##### 代码

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

##### 解法

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

##### 解法

```
由于题目假设nums[-1]=nums[n]=-∞。
所以，我们从0开始往后遍历元素，如果某个元素大于其后面的元素，则该元素就是峰值元素。（但是它时O(n)，不符合题意）

O(logN)一般考虑二分搜索。有如下规律：

规律一：如果nums[i] > nums[i+1]，则在i之前一定存在峰值元素

规律二：如果nums[i] < nums[i+1]，则在i+1之后一定存在峰值元素

(以上内容摘抄自[陈允怀_YahtoChen](https://leetcode-cn.com/u/archibald_/)的评论)
```

##### 代码

```python
class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
```

#### [164. 最大间距](https://leetcode-cn.com/problems/maximum-gap/)

##### 解法

```
这道题很简单鸭，是我想错了么。。。

1. 把每个数看成二进制的字符串
2. 看每个数的[个位]是不是1，是1就把这个数放在右边，否则就放左边
3. 看每个数的[十位]...
4. 看每个数的[百位]..
5. 一直看32次，看完后这个数组就是有序的了。。。
6. 时间复杂度是 32N 也就是N，空间复杂度也是N
```

##### 代码

```python
class Solution:
    def maximumGap(self, nums):
        if len(nums)<2:return 0
        for i in range(32):
            left, right = [], []
            for num in nums:
                if (1 << i) & num:
                    right.append(num)
                else:
                    left.append(num)
            nums = left + right
        rst = 0
        for i in range(1, len(nums)):
            rst = max(rst, nums[i]-nums[i-1])
        return rst
```

#### [165. 比较版本号](https://leetcode-cn.com/problems/compare-version-numbers/)

##### 解法

```
把传入的字符串按 '.' 分割，得到的每个部分转成整数，然后再挨个比较就可以了。
```

##### 代码

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

##### 解法

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

##### 解法

```
开始时，左指针指向最左边那个数，右指针指向最右边那个数。
要是两个指针对应的数加起来比目标值小，左指针右移一个单位；
要是两个指针对应的数加起来比目标值大，右指针左移一个单位；
要是两个指针对应的数加起来等于目标值，就返回结果。
```

##### 代码

```python
class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while True:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                break
        return left+1, right+1
            
```

#### [168. Excel表列名称](https://leetcode-cn.com/problems/excel-sheet-column-title/)

##### 解法

```
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

##### 解法

```
开始结果为空
遍历每个数字：
    结果为空：结果=此数字
    此数字跟结果相同，加一条命；
    此数字跟结果不同，减一条命；减到命为0了就把结果置空。
最终结果就是答案。
```

##### 代码

```python
class Solution(object):
    def majorityElement(self, nums):
        rst, life = None, 0
        for num in nums:
            if rst is None:
                rst = num
                life = 1
            elif rst == num:
                life += 1
            else:
                life -= 1
                if life == 0:
                    rst = None
        return rst
```

#### [171. Excel表列序号](https://leetcode-cn.com/problems/excel-sheet-column-number/)

##### 解法

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

##### 解法

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

##### 解法

```
直接把中序遍历的结果存到数组里，再依次输出。
```

##### 代码

```python
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.vals = []
        self.stack = [root]
        while self.stack:
            root = self.stack.pop(-1)
            if isinstance(root, int):
                self.vals.append(root)
            elif isinstance(root, TreeNode):
                self.stack.extend([root.right, root.val, root.left])
        self.i = 0

    def next(self):
        """
        :rtype: int
        """
        rst = self.vals[self.i]
        self.i += 1
        return rst


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i != len(self.vals)
```

#### [174. 地下城游戏](https://leetcode-cn.com/problems/dungeon-game/submissions/)

##### 解法

```
这是我蒙出来的，不好写解法。。
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

##### 解法

```
本质是排序题，将数组按照一定规则排序，再把所有数连在一起即可。
```

##### 代码

```python
from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        nums = [str(x) for x in nums]
        nums.sort(
            key=cmp_to_key(lambda x, y: 1 if x+y > y+x else -1), 
            reverse=True,
        )
        rst = "".join(nums)
        return '0' if rst[0] == '0' else rst
```

#### [187. 重复的DNA序列](https://leetcode-cn.com/problems/repeated-dna-sequences/)

##### 解法

```
用字典记录下所有长度为10的子串出现的次数。
```

##### 代码

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

##### 解法

```
你突然醒来，看看日历今天是第几天？看看自己手上有没有股票？看看自己还有几次买股票的机会？就可以做出抉择了。

如果今天是最后一天：
    且手上有股票，那就把手上的股票卖出去。
不是最后一天：
    手上有股票：卖股票和啥都不干选一个收益最大的。
    手上无股票：买股票（如果还可以购买）和啥都不干选一个收益最大的。
    
然后直接用递归硬撸就完事儿了！
```

##### 代码

```python
from functools import lru_cache


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        self.prices = prices
        return self.res(0, False, k)
    
    @lru_cache(None)
    def res(self, i, stock, k):
        if i >= len(self.prices)-1:  # 是最后一天
            if stock:
                return self.prices[i]
            else:
                return 0
        elif stock:  # 可以卖
            return max(
                self.res(i+1, True, k),
                self.res(i+1, False, k) + self.prices[i],
            )
        else:  # 手上没股票
            if k > 0:
                return max(
                    self.res(i+1, False, k),
                    self.res(i+1, True, k-1) - self.prices[i],
                )
            else:
                return self.res(i+1, False, k)
                
```

#### [旋转数组](https://leetcode-cn.com/problems/rotate-array/)

##### 解法

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

#### [190. 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/)

##### 解法

```
每次取个位数字，连取32次。
```

##### 代码

```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rst = 0
        for _ in range(32):
            rst = (rst << 1) + (n & 1)
#             print(rst)
            n = n >> 1
        return rst
```

#### [191. 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits/)

##### 解法

```
判断个位数是不是1，重复很多次。
```

##### 代码

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

##### 解法

```
房间的下标i，有没有偷钱f，(i, f)可以代表一个状态。res(i, f)表示在(i, f)状态下，可以最大偷多少钱。
```

##### 代码

```python
# 递归版
from functools import lru_cache


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        self.nums = nums
        return max(self.res(0, 0), self.res(0, 1) + self.nums[0])
    
    @lru_cache(None)
    def res(self, i, f):
        if i >= len(self.nums)-1:
            return 0
        if f:
            return self.res(i+1, 0)
        else:
            return max(
                self.res(i+1, 0),
                self.res(i+1, 1) + self.nums[i+1],
            )
```

数组版
```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        for i in range(n-2, -1, -1):
            dp[i][1] = dp[i+1][0]
            dp[i][0] = max(dp[i+1][0], dp[i+1][1] + nums[i+1])
        return max(dp[0][0], dp[0][1] + nums[0])
```

#### [199. 二叉树的右视图](https://leetcode-cn.com/problems/binary-tree-right-side-view/)

##### 解法

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

##### 解法

```
广度搜索。
```

##### 代码

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        k = 0
        
        for i in range(m):
            for j in range(n):
                if self.bfs(grid, i, j):
                    k += 1
        
        return k
    
    def bfs(self, grid, i, j):
        if grid[i][j] == "1":
            grid[i][j] = '9'
            for (r, c) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= r < len(grid) and (0 <= c < len(grid[0])):
                    self.bfs(grid, r, c)
            return True
```