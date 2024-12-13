# https://leetcode.com/problems/n-queens-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def __init__(self):
        self.result = 0

    # Solution 1
    # O(n! * n) time / O(n * n) space
    def totalNQueens(self, n):
        self.result = 0
        self.dfs(n, 0, set())
        return self.result

    def dfs(self, n, row, positions):
        if row == n:
            self.result += 1
            return

        for col in range(n):
            if (row, col) in positions:
                continue
            self.dfs(n, row + 1, positions | self.getPositions(n, row, col))

    def getPositions(self, n, row, col):
        positions = set()
        # HORIZONTAL
        for j in range(n):
            positions.add((row, j))

        # VERTICAL
        for i in range(n):
            positions.add((i, col))

        # DIAGONALS
        i, j = row, col
        while i >= 0 and j >= 0:
            positions.add((i, j))
            i -= 1
            j -= 1

        i, j = row, col
        while i < n and j < n:
            positions.add((i, j))
            i += 1
            j += 1

        i, j = row, col
        while i >= 0 and j < n:
            positions.add((i, j))
            i -= 1
            j += 1

        i, j = row, col
        while i < n and j >= 0:
            positions.add((i, j))
            i += 1
            j -= 1

        return positions


if __name__ == '__main__':
    solution = Solution()
    print(solution.totalNQueens(n=4))
    print(solution.totalNQueens(n=1))
