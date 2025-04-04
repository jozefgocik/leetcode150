# https://leetcode.com/problems/unique-paths-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) time / O(n * m) space
    def uniquePathsWithObstacles(self, obstacleGrid):
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        cache[ROWS - 1][COLS - 1] = 1

        for i in reversed(range(ROWS)):
            for j in reversed(range(COLS)):
                if obstacleGrid[i][j] == 0 and i == ROWS - 1 and j == COLS - 1:
                    continue
                if obstacleGrid[i][j] == 0:
                    down, right = cache[i + 1][j], cache[i][j + 1]
                    cache[i][j] = down + right
                else:
                    cache[i][j] = 0

        return cache[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(solution.uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]))
