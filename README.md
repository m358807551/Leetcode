# Leetcode
用最短的代码或最简单的思路做成的力扣题解。

#### [134. 加油站](https://leetcode-cn.com/problems/gas-station/)

##### 解法

```
有一个环形路上有n个站点； 每个站点都有一个好人或一个坏人； 好人会给你钱，坏人会收你一定的过路费，如果你带的钱不够付过路费，坏人会跳起来把你砍死； 问：从哪个站点出发，能绕一圈活着回到出发点?

首先考虑一种情况：如果全部好人给你 的钱加起来 小于 坏人收的过路费之和，那么总有一次你的钱不够付过路费，你的结局注定会被砍死。

假如你随机选一点 start 出发，那么你肯定会选一个有好人的站点开始，因为开始的时候你没有钱，遇到坏人只能被砍死；

现在你在start出发，走到了某个站点end，被end站点的坏人砍死了，说明你在 [start, end) 存的钱不够付 end点坏人的过路费，因为start站点是个好人，所以在 (start, end) 里任何一点出发，你存的钱会比现在还少，还是会被end站点的坏人砍死；

于是你重新读档，聪明的选择从 end+1点出发，继续你悲壮的征程； 终于有一天，你发现自己走到了尽头（下标是n-1)的站点而没有被砍死； 此时你犹豫了一下，那我继续往前走，身上的钱够不够你继续走到出发点Start?

当然可以，因为开始已经判断过，好人给你的钱数是大于等于坏人要的过路费的，你现在攒的钱完全可以应付 [0, start) 这一段坏人向你收的过路费。 这时候你的嘴角微微上扬，眼眶微微湿润，因为你已经知道这个世界的终极奥秘：Start就是这个问题的答案。
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

