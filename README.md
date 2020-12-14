# Leetcode
用最短的代码或最简单的思路做成的力扣题解。

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

