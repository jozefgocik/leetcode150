# https://leetcode.com/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # # O(n) time / O(n) space
    # def getMinimumDifference(self, root):
    #     array = self.getMinimumDifferenceHelper(root, [])
    #     result = float("inf")
    #     for i in range(len(array) - 1):
    #         result = min(result, abs(array[i] - array[i + 1]))
    #
    #     return result
    #
    # def getMinimumDifferenceHelper(self, root, array):
    #     if not root:
    #         return array
    #
    #     self.getMinimumDifferenceHelper(root.left, array)
    #     array.append(root.val)
    #     self.getMinimumDifferenceHelper(root.right, array)
    #
    #     return array

    # Solution 2
    # O(n) time / O(d) space
    result = float("inf")
    lastValue = float("inf")

    def getMinimumDifference(self, root):
        def dfs(current):
            if current.left:
                dfs(current.left)
            self.result = min(self.result, abs(current.val - self.lastValue))
            self.lastValue = current.val
            if current.right:
                dfs(current.right)

        dfs(root)
        return self.result
