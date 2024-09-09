# https://leetcode.com/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) time / O(n * m) space
    # def gameOfLife(self, board):
    #     temp = [[board[i][j] for j in range(len(board[i]))] for i in range(len(board))]
    #
    #     for i in range(len(temp)):
    #         for j in range(len(temp[i])):
    #             liveNeighbours = 0
    #             indices = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1],
    #                        [i, j - 1], [i, j + 1],
    #                        [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]
    #             for pair in indices:
    #                 row, col = pair
    #                 if row not in range(len(temp)) or col not in range(len(temp[i])):
    #                     continue
    #                 elif temp[row][col] == 1:
    #                     liveNeighbours += 1
    #
    #             if temp[i][j] == 1:
    #                 if liveNeighbours in range(2, 4):
    #                     board[i][j] = 1
    #                 else:
    #                     board[i][j] = 0
    #             elif liveNeighbours == 3:
    #                 board[i][j] = 1
    #             else:
    #                 board[i][j] = temp[i][j]
    #
    #     return board

    # Solution 2
    # Original | New | State
    #     0    |  0  | -> 0
    #     1    |  0  | -> 1
    #     0    |  1  | -> 2
    #     1    |  1  | -> 3
    # O(n * m) time / O(1) space
    def gameOfLife(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                liveNeighbours = self.numberOfNeighbous(board, i, j)

                if board[i][j] == 1:
                    if liveNeighbours in [2, 3]:
                        board[i][j] = 3
                elif liveNeighbours == 3:
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in [2, 3]:
                    board[i][j] = 1

        return board

    def numberOfNeighbous(self, board, i, j):
        liveNeighbours = 0
        indices = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1],
                   [i, j - 1], [i, j + 1],
                   [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]
        for pair in indices:
            row, col = pair
            if row not in range(len(board)) or col not in range(len(board[i])):
                continue
            elif board[row][col] in [1, 3]:
                liveNeighbours += 1

        return liveNeighbours


if __name__ == '__main__':
    solution = Solution()
    print(solution.gameOfLife(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
    print(solution.gameOfLife(board=[[1, 1], [1, 0]]))
