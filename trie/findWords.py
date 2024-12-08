# https://leetcode.com/problems/word-search-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(m * n) time / O(m * n) space
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        result, visited = [], set()
        for i in list(range(len(board))):
            for j in list(range(len(board[i]))):
                self.dfs(board, result, i, j, trie.root, "")

        return result

    def dfs(self, board, result, i, j, node, word):
        if node.isWord:
            result.append(word)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        temp = board[i][j]
        node = node.children.get(temp)
        if not node:
            return

        board[i][j] = "#"
        self.dfs(board, result, i + 1, j, node, word + temp)
        self.dfs(board, result, i - 1, j, node, word + temp)
        self.dfs(board, result, i, j - 1, node, word + temp)
        self.dfs(board, result, i, j + 1, node, word + temp)
        board[i][j] = temp


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True


if __name__ == '__main__':
    solution = Solution()
    print(solution.findWords(
        board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        words=["oath", "pea", "eat", "rain"]))
    print(solution.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))
