"""
https://leetcode-cn.com/problems/lru-cache
"""


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.th, self.tt = Node(None, None), Node(None, None)
        self.th.next = self.tt
        self.tt.pre = self.th
        self.key2node = {}
        self.n = capacity

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def insert_after(self, pre, node):
        next_ = pre.next
        pre.next = node
        node.next = next_
        next_.pre = node
        node.pre = pre

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.key2node.get(key)
        if not node:
            return -1
        self.remove(node)
        self.insert_after(self.th, node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.key2node.get(key)
        if not node:
            if len(self.key2node) == self.n:
                self.key2node.pop(self.tt.pre.key)
                self.remove(self.tt.pre)

            node = Node(key, value)
            self.insert_after(self.th, node)
            self.key2node[key] = node
        else:
            node.val = value
            self.remove(node)
            self.insert_after(self.th, node)

    def show(self):
        p = self.th.next
        rst = []
        while p is not self.tt:
            rst.append('{}:{}'.format(p.key, p.val))
            p = p.next
        print('show: ' + '->'.join(rst))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def main():
    lru = LRUCache(2)
    print("lru.put(1, 1)", lru.put(1, 1))
    lru.show()

    print("lru.put(2, 2)", lru.put(2, 2))
    lru.show()

    print("lru.get(1)", lru.get(1))
    lru.show()

    print("lru.put(3, 3)", lru.put(3, 3))
    lru.show()

    print(lru.get(2))
    lru.show()

    lru.put(4, 4)
    lru.show()

    print(lru.get(1))
    lru.show()

    print(lru.get(3))
    lru.show()

    print(lru.get(4))
    lru.show()


if __name__ == '__main__':
    main()
