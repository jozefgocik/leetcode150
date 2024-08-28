# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    # Solution 1
    # O(n ^ 2) time / O(n) space
    # def isValidSudoku(self, board):
    #     areColumnsValid = self.checkColumns(board)
    #     areRowsValid = self.checkRows(board)
    #     areBoxesValid = self.checkBoxes(board)
    #
    #     return areColumnsValid and areRowsValid and areBoxesValid
    #
    # def checkColumns(self, board):
    #     for i in range(len(board)):
    #         charSet = set()
    #         for j in range(len(board[i])):
    #             if board[j][i] == ".":
    #                 continue
    #             elif board[j][i] not in charSet:
    #                 charSet.add(board[j][i])
    #             else:
    #                 return False
    #
    #     return True
    #
    # def checkRows(self, board):
    #     for i in range(len(board)):
    #         charSet = set()
    #         for j in range(len(board[i])):
    #             if board[i][j] == ".":
    #                 continue
    #             elif board[i][j] not in charSet:
    #                 charSet.add(board[i][j])
    #             else:
    #                 return False
    #
    #     return True
    #
    # def checkBoxes(self, board):
    #     startColIndex = 0
    #     charSet = set()
    #     i = 0
    #     while i < len(board):
    #         for j in range(startColIndex, len(board[i])):
    #             if j != startColIndex and j % 3 == 0:
    #                 break
    #
    #             if board[i][j] == ".":
    #                 continue
    #             elif board[i][j] not in charSet:
    #                 charSet.add(board[i][j])
    #             else:
    #                 return False
    #
    #         if (i + 1) % 3 == 0:
    #             charSet = set()
    #
    #         if i == len(board) - 1 and startColIndex < len(board[i]) - 3:
    #             i = -1
    #             startColIndex += 3
    #
    #         i += 1
    #
    #     return True

    # Solution 2
    # O(n ^ 2) time / O(n ^ 2) space
    def isValidSudoku(self, board):
        rows, cols, boxes = {}, {}, {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                currentChar = board[i][j]
                if currentChar == ".":
                    continue

                if i not in rows:
                    rows[i] = set()
                if currentChar in rows[i]:
                    return False
                rows[i].add(currentChar)

                if j not in cols:
                    cols[j] = set()
                if currentChar in cols[j]:
                    return False
                cols[j].add(currentChar)

                boxesKey = str(i // 3) + str(j // 3)
                if boxesKey not in boxes:
                    boxes[boxesKey] = set()
                if currentChar in boxes[boxesKey]:
                    return False
                boxes[boxesKey].add(currentChar)

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSudoku(board=
                                 [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(solution.isValidSudoku(board=
                                 [["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
