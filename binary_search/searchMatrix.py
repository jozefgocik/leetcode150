# https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(log(n * m)) time / O(n) space
    def searchMatrix(self, matrix, target):
        row = self.getRow(matrix, target)

        return self.contains(matrix[row], target)

    def getRow(self, matrix, target):
        left, right = 0, len(matrix) - 1

        while left < right:
            index = (left + right) // 2

            if matrix[index][-1] < target:
                left = index + 1
            elif matrix[index][0] > target:
                right = index - 1
            else:
                return index

        return left

    def contains(self, array, target):
        left, right = 0, len(array) - 1

        while left <= right:
            index = (left + right) // 2

            if array[index] == target:
                return True
            if array[index] < target:
                left = index + 1
            else:
                right = index - 1

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
    print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
