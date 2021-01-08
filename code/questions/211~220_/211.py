"""
https://leetcode-cn.com/problems/add-and-search-word-data-structure-design
"""


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        dic = self.d
        for c in word:
            dic = dic.setdefault(c, {})
        dic['#'] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(self.d, word)

    def _search(self, d, word):
        if not word:
            return d.get('#', False)
        if word[0] == '.':
            for sub_d in d.values():
                if isinstance(sub_d, dict) and self._search(sub_d, word[1:]):
                    return True
            return False
        else:
            if word[0] in d:
                return self._search(d[word[0]], word[1:])
            else:
                return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
for word in ["bad","dad","mad",]:
    obj.addWord(word)

for pat in ["b.."]:
    print(obj.search(pat))
