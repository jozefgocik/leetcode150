# https://leetcode.com/problems/rotate-image/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(1) space
    def rotate(self, matrix):
        startCol, endCol = 0, len(matrix) - 1
        while startCol < endCol:
            for i in range(endCol - startCol):
                startRow, endRow = startCol, endCol

                temp = matrix[startRow][startCol + i]

                # move top left to top right
                matrix[startRow + i][endCol], temp = temp, matrix[startRow + i][endCol]
                # move top right to bottom right
                matrix[endRow][endCol - i], temp = temp, matrix[endRow][endCol - i]
                # move bottom right to bottom left
                matrix[endRow - i][startCol], temp = temp, matrix[endRow - i][startCol]
                # move bottom left to top left
                matrix[startRow][startCol + i] = temp

            startCol += 1
            endCol -= 1

        return matrix


if __name__ == '__main__':
    solution = Solution()
    print(solution.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution.rotate(matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
