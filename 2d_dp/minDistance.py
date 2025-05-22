# https://leetcode.com/problems/edit-distance/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) time / O(n * m) space
    # def minDistance(self, word1, word2):
    #     cache = {}
    #
    #     def dfs(i, j):
    #         if i == len(word1):
    #             return len(word2) - j
    #         if j == len(word2):
    #             return len(word1) - i
    #         if (i, j) in cache:
    #             return cache[(i, j)]
    #
    #         if word1[i] == word2[j]:
    #             result = dfs(i + 1, j + 1)
    #         else:
    #             replace = dfs(i + 1, j + 1)
    #             insert = dfs(i, j + 1)
    #             delete = dfs(i + 1, j)
    #             result = 1 + min(replace, insert, delete)
    #
    #         cache[(i, j)] = result
    #         return result
    #
    #     return dfs(0, 0)

    # Solution 2
    # O(n * m) time / O(n * m) space
    def minDistance(self, word1, word2):
        cache = [[float("inf") for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j

        for i in reversed(range(len(word1))):
            for j in reversed(range(len(word2))):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    insert = cache[i + 1][j]
                    delete = cache[i][j + 1]
                    replace = cache[i + 1][j + 1]
                    cache[i][j] = 1 + min(insert, delete, replace)

        return cache[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance(word1="horse", word2="ros"))
    print(solution.minDistance(word1="intention", word2="execution"))
    print(solution.minDistance(word1="sea", word2="eat"))
