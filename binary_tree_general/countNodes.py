# https://leetcode.com/problems/count-complete-tree-nodes/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(log(n) * log(n)) time / O(d) space
    def countNodes(self, root):
        if not root:
            return 0

        l, r = self.leftHeight(root), self.rightHeight(root)

        if l > r:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
        else:
            return (2 ** l) - 1

    def leftHeight(self, root):
        if not root:
            return 0

        return self.leftHeight(root.left) + 1

    def rightHeight(self, root):
        if not root:
            return 0

        return self.rightHeight(root.right) + 1
