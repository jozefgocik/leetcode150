# https://leetcode.com/problems/construct-quad-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):

    # Solution 1
    # O(n^2 * log(n)) time / O(n^2 * log(n)) space
    # def construct(self, grid):
    #     if self.isLeaf(grid):
    #         return Node(grid[0][0] == 1, True)
    #
    #     topLeftGrid, topRightGrid, bottomLeftGrid, bottomRightGrid = self.getSubgrids(grid)
    #     topLeft = self.construct(topLeftGrid)
    #     topRight = self.construct(topRightGrid)
    #     bottomLeft = self.construct(bottomLeftGrid)
    #     bottomRight = self.construct(bottomRightGrid)
    #
    #     return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
    #
    # def getSubgrids(self, grid):
    #     topLeft, topRight, bottomLeft, bottomRight = [], [], [], []
    #     n = len(grid) // 2
    #     for row in range(n):
    #         topLeft.append([])
    #         for col in range(n):
    #             topLeft[row].append(grid[row][col])
    #
    #     for row in range(n):
    #         topRight.append([])
    #         for col in range(n, len(grid)):
    #             topRight[row].append(grid[row][col])
    #
    #     for row in range(n, len(grid)):
    #         bottomLeft.append([])
    #         for col in range(n):
    #             bottomLeft[row % n].append(grid[row][col])
    #
    #     for row in range(n, len(grid)):
    #         bottomRight.append([])
    #         for col in range(n, len(grid)):
    #             bottomRight[row % n].append(grid[row][col])
    #
    #     return topLeft, topRight, bottomLeft, bottomRight
    #
    # def isLeaf(self, grid):
    #     char = grid[0][0]
    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #             if grid[i][j] != char:
    #                 return False
    #
    #     return True

    # Solution 2
    # O(n^2 * log(n)) time / O(n^2) space
    def construct(self, grid):
        return self.constructHelper(grid, len(grid), 0, 0)

    def constructHelper(self, grid, n, row, col):
        if self.isLeaf(grid, n, row, col):
            return Node(grid[row][col] == 1, True)

        n = n // 2
        topLeft = self.constructHelper(grid, n, row, col)
        topRight = self.constructHelper(grid, n, row, col + n)
        bottomLeft = self.constructHelper(grid, n, row + n, col)
        bottomRight = self.constructHelper(grid, n, row + n, col + n)

        return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

    def isLeaf(self, grid, n, row, col):
        char = grid[row][col]
        for i in range(n):
            for j in range(n):
                if grid[row + i][col + j] != char:
                    return False

        return True
