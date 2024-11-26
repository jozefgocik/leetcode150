# https://leetcode.com/problems/word-ladder/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(n ^ 2) space; n = len(wordList)
    # def ladderLength(self, beginWord, endWord, wordList):
    #     nodes = {}
    #     if beginWord not in wordList:
    #         wordList.append(beginWord)
    #     for word in wordList:
    #         nodes[word] = []
    #         for child in wordList:
    #             if self.countDifferences(word, child) == 1:
    #                 nodes[word].append(child)
    #
    #     queue = [[beginWord, 1]]
    #     visited = set()
    #     while queue:
    #         current, count = queue.pop(0)
    #         visited.add(current)
    #
    #         if current == endWord:
    #             return count
    #
    #         for child in nodes[current]:
    #             if child not in visited:
    #                 queue.append([child, count + 1])
    #
    #     return 0
    #
    # def countDifferences(self, word1, word2):
    #     result = 0
    #     for i in range(min(len(word1), len(word2))):
    #         if word1[i] != word2[i]:
    #             result += 1
    #     return result

    # Solution 2
    # O(n * (m ^ 2)) time / O(n ^ 2) space; n = len(wordList), m = len(beginWord)
    def ladderLength(self, beginWord, endWord, wordList):
        nodes = {}
        if beginWord not in wordList:
            wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[0:i] + "*" + word[i+1:]
                if pattern not in nodes:
                    nodes[pattern] = []
                nodes[pattern].append(word)

        queue = [[beginWord, 1]]
        visited = set()
        while queue:
            current, count = queue.pop(0)
            visited.add(current)

            if current == endWord:
                return count

            for i in range(len(current)):
                pattern = current[0:i] + "*" + current[i+1:]
                for child in nodes[pattern]:
                    if child not in visited:
                        queue.append([child, count + 1])

        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution.ladderLength(beginWord="hog", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))
