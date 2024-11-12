# https://leetcode.com/problems/validate-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def isValidBST(self, root):
    #     array = self.isValidBSTHelper(root, [])
    #
    #     for i in range(len(array) - 1):
    #         if array[i] >= array[i + 1]:
    #             return False
    #
    #     return True
    #
    # def isValidBSTHelper(self, root, array):
    #     if not root:
    #         return array
    #
    #     self.isValidBSTHelper(root.left, array)
    #     array.append(root.val)
    #     self.isValidBSTHelper(root.right, array)
    #
    #     return array

    # Solution 2
    # O(n) time / O(n) space
    # def isValidBST(self, root):
    #     queue = [[root, float("-inf"), float("inf")]]
    #
    #     while queue:
    #         node, minimum, maximum = queue.pop(0)
    #
    #         if node.val >= maximum or node.val <= minimum:
    #             return False
    #
    #         if node.left:
    #             queue.append([node.left, minimum, node.val])
    #         if node.right:
    #             queue.append([node.right, node.val, maximum])
    #
    #     return True

    # Solution 3
    # O(n) time / O(d) space
    def isValidBST(self, root):
        return self.isValidBSTHelper(root, float("-inf"), float("inf"))

    def isValidBSTHelper(self, root, minimum, maximum):
        if not root:
            return True
        if root.val >= maximum or root.val <= minimum:
            return False

        return self.isValidBSTHelper(root.left, minimum, root.val) and self.isValidBSTHelper(root.right, root.val, maximum)
