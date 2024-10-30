# https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # Solution 1
    # O(n) time / O(d) space
    def maxPathSum(self, root):
        return self.maxPathSumHelper(root)[1]

    def maxPathSumHelper(self, root):
        if not root:
            return float("-inf"), float("-inf")

        left, leftResult = self.maxPathSumHelper(root.left)
        right, rightResult = self.maxPathSumHelper(root.right)

        maxToReturn = max(left + root.val, right + root.val, root.val)
        result = max(maxToReturn, leftResult, rightResult, left, right, left + right + root.val)

        return maxToReturn, result
