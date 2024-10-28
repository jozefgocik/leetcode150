# https://leetcode.com/problems/path-sum/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n) time / O(d) space
    def hasPathSum(self, root, targetSum, currentSum=0):
        if not root:
            return False
        if root and root.left is None and root.right is None:
            return currentSum + root.val == targetSum

        return self.hasPathSum(root.left, targetSum, currentSum + root.val) or self.hasPathSum(root.right, targetSum, currentSum + root.val)

