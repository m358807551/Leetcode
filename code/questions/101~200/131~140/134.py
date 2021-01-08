"""
https://leetcode-cn.com/problems/gas-station
"""


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


def main():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(
        Solution().canCompleteCircuit(
            gas,
            cost,
        )
    )


if __name__ == '__main__':
    main()
