# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(n) space
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        midIdx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:midIdx + 1], inorder[:midIdx])
        root.right = self.buildTree(preorder[midIdx + 1:], inorder[midIdx + 1:])

        return root
