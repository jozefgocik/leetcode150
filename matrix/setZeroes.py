# https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) time / O(1) space
    def setZeroes(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    # left part of the row
                    for col in range(j):
                        matrix[i][col] = None
                    # right part of the row
                    for col in range(j + 1, len(matrix[i])):
                        if matrix[i][col] != 0:
                            matrix[i][col] = None
                    # upper part of the col
                    for row in range(i):
                        matrix[row][j] = None
                    # lower part of the col
                    for row in range(i + 1, len(matrix)):
                        if matrix[row][j] != 0:
                            matrix[row][j] = None

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0

        return matrix


if __name__ == '__main__':
    solution = Solution()
    print(solution.setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(solution.setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
