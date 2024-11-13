# https://leetcode.com/problems/number-of-islands/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) time / O(n * m) space
    def numIslands(self, grid):
        result = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == "1":
                    visited.add((i, j))
                    self.bfs(grid, i, j, visited)
                    result += 1

        return result

    def bfs(self, grid, i, j, visited):
        queue = [(i, j)]
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        while queue:
            i, j = queue.pop(0)
            for direction in directions:
                row, col = i + direction[0], j + direction[1]
                if (row in range(len(grid)) and col in range(len(grid[row]))
                        and grid[row][col] == "1" and (row, col) not in visited):
                    visited.add((row, col))
                    queue.append((row, col))


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))
    print(solution.numIslands(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))

    print(solution.numIslands(grid=[
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ]))
