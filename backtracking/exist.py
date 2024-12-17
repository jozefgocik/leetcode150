# https://leetcode.com/problems/word-search/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m * 4^n) time / O(n * m) space
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.existHelper(board, word, set(), i, j, 0):
                    return True

        return False

    def existHelper(self, board, word, visited, row, col, i):
        if i == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or word[i] != board[row][col] or (row, col) in visited:
            return False

        visited.add((row, col))
        up = self.existHelper(board, word, visited, row - 1, col, i + 1)
        left = self.existHelper(board, word, visited, row, col - 1, i + 1)
        down = self.existHelper(board, word, visited, row + 1, col, i + 1)
        right = self.existHelper(board, word, visited, row, col + 1, i + 1)
        visited.remove((row, col))

        return up or left or down or right


if __name__ == '__main__':
    solution = Solution()
    print(solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
    print(solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
    print(solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))
