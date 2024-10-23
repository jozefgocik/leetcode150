# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(n) time
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        midIdx = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[0:midIdx], postorder[0:midIdx])
        root.right = self.buildTree(inorder[midIdx + 1:], postorder[midIdx:len(postorder) - 1])

        return root
