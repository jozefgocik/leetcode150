# https://leetcode.com/problems/minimum-path-sum/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) time / O(n * m) space
    def minPathSum(self, grid):
        cache = [[float("inf") for _ in range(len(grid[0]) + 1)] for i in range(len(grid) + 1)]
        cache[0][1], cache[1][0] = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                left = cache[i + 1][j]
                up = cache[i][j + 1]
                cache[i + 1][j + 1] = grid[i][j] + min(left, up)

        return cache[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(solution.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
