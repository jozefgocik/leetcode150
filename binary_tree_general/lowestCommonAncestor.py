# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Solution 1
    # O(n) time / O(d) space
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        leftSubtree = self.lowestCommonAncestor(root.left, p, q)
        rightSubtree = self.lowestCommonAncestor(root.right, p, q)
        current = None
        if root == p or root == q:
            current = root

        if (leftSubtree and rightSubtree) or (current and leftSubtree) or (current and rightSubtree):
            return root

        return leftSubtree or rightSubtree or current
