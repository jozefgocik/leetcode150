# https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def invertTree(self, root):
    #     queue = [root]
    #
    #     while queue:
    #         current = queue.pop(0)
    #         if current:
    #             current.left, current.right = current.right, current.left
    #             queue.append(current.left)
    #             queue.append(current.right)
    #
    #     return root

    # Solution 2
    # O(n) time / O(d) space
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
