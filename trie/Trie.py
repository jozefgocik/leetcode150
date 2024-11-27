# https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150

class Trie(object):

    # Solution 1
    # O(w * l) time / O(w * l) space; w = number of words, l = avg length of words
    def __init__(self):
        self.root = {}

    def insert(self, word):
        root = self.root
        for char in word:
            if char not in root:
                root[char] = {}
            root = root[char]
        root[""] = None

    def search(self, word):
        root = self.root
        for char in word:
            if char not in root:
                return False
            root = root[char]

        return "" in root

    def startsWith(self, prefix):
        root = self.root
        for char in prefix:
            if char not in root:
                return False
            root = root[char]

        return True


if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    obj = Trie()
    word = "apple"
    prefix = "app"
    obj.insert(word)
    obj.insert("app")
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)
