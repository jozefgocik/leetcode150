# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n) time / O(d) space
    # def flatten(self, root):
    #     if not root:
    #         return None
    #
    #     nextNode = self.flatten(root.right)
    #     root.right = self.flatten(root.left)
    #     temp = root
    #     while temp is not None and temp.right is not None:
    #         temp = temp.right
    #     if temp is not None:
    #         temp.right = nextNode
    #     root.left = None
    #
    #     return root

    # Solution 2
    # O(n) time / O(d) space
    def flatten(self, root):
        def dfs(current):
            if not current:
                return None

            leftTail = dfs(current.left)
            rightTail = dfs(current.right)

            if leftTail:
                leftTail.right = current.right
                current.right = current.left
                current.left = None

            return rightTail or leftTail or current

        dfs(root)
