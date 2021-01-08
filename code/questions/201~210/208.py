"""
https://leetcode-cn.com/problems/implement-trie-prefix-tree
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = set()
        self.is_end = False

    def find_child(self, val):
        for child in self.children:
            if val == child.val:
                return child
        return None


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self._insert(self.root, word)

    def _insert(self, root, word):
        the_child = root.find_child(word[0])
        if not the_child:
            the_child = Node(word[0])
            root.children.add(the_child)
        if len(word) == 1:
            the_child.is_end = True
        else:
            self._insert(the_child, word[1:])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self._search(self.root, word)

    def _search(self, root, word):
        the_child = root.find_child(word[0])
        if not the_child:
            return False
        if len(word) == 1:
            return the_child.is_end
        return self._search(the_child, word[1:])


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self._startswith(self.root, prefix)

    def _startswith(self, root, word):
        the_child = root.find_child(word[0])
        if not the_child:
            return False
        if len(word) == 1:
            return True
        return self._startswith(the_child, word[1:])

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
print(obj.startsWith('app'))
print(obj.search('app'))
print(obj.search('apple'))
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
