# https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) time / O(1) space
    def spiralOrder(self, matrix):
        result = []
        startCol, endCol = 0, len(matrix[0])
        startRow, endRow = 0, len(matrix)

        while startCol < endCol and startRow < endRow:
            for col in range(startCol, endCol):
                result.append(matrix[startRow][col])
            startRow += 1

            for row in range(startRow, endRow):
                result.append(matrix[row][endCol - 1])
            endCol -= 1

            if not (startCol < endCol and startRow < endRow):
                break

            for col in reversed(range(startCol, endCol)):
                result.append(matrix[endRow - 1][col])
            endRow -= 1

            for row in reversed(range(startRow, endRow)):
                result.append(matrix[row][startCol])
            startCol += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(solution.spiralOrder(matrix=[[1], [4], [7]]))
    print(solution.spiralOrder(matrix=[[1, 2, 3]]))
