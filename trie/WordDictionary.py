# https://leetcode.com/problems/design-add-and-search-words-data-structure/?envType=study-plan-v2&envId=top-interview-150

class WordDictionary(object):

    # Solution 1
    # O(w * l) time / O(w * l) space; w = number of words, l = avg length of words
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        root = self.root
        for char in word:
            if char not in root:
                root[char] = {}
            root = root[char]
        root[""] = None

    def search(self, word):
        return self.searchHelper(word, self.root)

    def searchHelper(self, word, root):
        if not root:
            return False
        if word == "":
            return root and "" in root
        if word[0] == ".":
            for r in root:
                result = self.searchHelper(word[1:], root[r])
                if result:
                    return True
        if word[0] in root:
            return self.searchHelper(word[1:], root[word[0]])

        return False


if __name__ == '__main__':
    # Your WordDictionary object will be instantiated and called as such:
    obj = WordDictionary()
    word = "bad"
    obj.addWord(word)
    param_2 = obj.search(word)
