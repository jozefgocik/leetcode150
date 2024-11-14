# https://leetcode.com/problems/surrounded-regions/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) time / O(n * m) space
    # def solve(self, board):
    #     visited = set()
    #
    #     # first row
    #     for j in range(len(board[0])):
    #         if board[0][j] == "O" and (0, j) not in visited:
    #             self.bfs(board, 0, j, visited)
    #     # last col
    #     for i in range(len(board)):
    #         if board[i][len(board[i]) - 1] == "O" and (i, len(board[i]) - 1) not in visited:
    #             self.bfs(board, i,  len(board[i]) - 1, visited)
    #     # last row
    #     for j in range(len(board[len(board) - 1])):
    #         if board[len(board) - 1][j] == "O" and (len(board) - 1, j) not in visited:
    #             self.bfs(board, len(board) - 1, j, visited)
    #     # first col
    #     for i in range(len(board)):
    #         if board[i][0] == "O" and (i, 0) not in visited:
    #             self.bfs(board, i,  0, visited)
    #
    #     for i in range(len(board)):
    #         for j in range(len(board[i])):
    #             if board[i][j] == "O" and (i, j) not in visited:
    #                 board[i][j] = "X"
    #
    #     return board
    #
    # def bfs(self, board, row, col, visited):
    #     queue = [(row, col)]
    #
    #     while queue:
    #         current = queue.pop(0)
    #         visited.add(current)
    #         directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    #         for direction in directions:
    #             i, j = current[0] + direction[0], current[1] + direction[1]
    #             if i in range(len(board)) and j in range(len(board[i])) and board[i][j] == "O" and (i, j) not in visited:
    #                 queue.append((i, j))

    # Solution 2
    # O(n * m) time / O(n * m) space
    def solve(self, board):
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited or board[row][col] == "X":
                return
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS - 1)

        for j in range(COLS):
            dfs(0, j)
            dfs(ROWS - 1, j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"

        return board


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve(board=[
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]))
    print(solution.solve(board=[
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "O", "X"]
    ]))
