# https://leetcode.com/problems/maximal-square/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(m * n) time / O(m * n) space
    def maximalSquare(self, matrix):
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == 0:
                return 0

            down = dfs(i + 1, j)
            diagonal = dfs(i + 1, j + 1)
            right = dfs(i, j + 1)

            result = 0 if matrix[i][j] == "0" else 1 + min(down, diagonal, right)
            cache[(i, j)] = result
            return result

        dfs(0, 0)
        return max(cache.values()) ** 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximalSquare(
        matrix=[["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]]))
    print(solution.maximalSquare(matrix=[["0", "1"], ["1", "0"]]))
    print(solution.maximalSquare(matrix=[["0"]]))
