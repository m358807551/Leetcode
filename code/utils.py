# coding=utf-8

"""辅助函数，通常用于生成一些结构便于测试."""
import json


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return '{}'.format(self.val)


def make_tree(vals):
    """通过层序遍历构建树."""
    if isinstance(vals, str):
        vals = json.loads(vals)
    if not vals:
        return None
    root = Node(vals.pop(0))
    queue = [root]
    while queue:
        cur = queue.pop(0)
        left_val = vals.pop(0) if vals else None
        if left_val is not None:
            cur.left = Node(left_val)
            queue.append(cur.left)
        right_val = vals.pop(0) if vals else None
        if right_val is not None:
            cur.right = Node(right_val)
            queue.append(cur.right)
    return root


def show(root):
    """层序遍历."""
    rst = []
    queue = [[root]]
    while queue:
        line = [
            node.val if node is not None else node
            for nodes in queue
            for node in nodes
        ]
        rst.extend(line)
        queue = [
            [node.left, node.right]
            for nodes in queue
            for node in nodes
            if node
        ]
    while rst[-1] is None:
        rst.pop(-1)
    return json.dumps(rst)


if __name__ == '__main__':
    a = make_tree('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')
    print(show(a))

