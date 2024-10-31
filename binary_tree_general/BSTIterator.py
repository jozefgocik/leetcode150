# https://leetcode.com/problems/binary-search-tree-iterator/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class BSTIterator(object):
#     # Solution 1
#     # O(n) time / O(d) space
#     def __init__(self, root):
#         self.tree = self.dfs(root)
#         self.current = TreeNode(-1, None, self.tree)
#
#     def dfs(self, root):
#         if not root:
#             return None
#
#         nextNode = self.dfs(root.right)
#         root.right = nextNode
#         previousNode = self.dfs(root.left)
#         if previousNode:
#             tempPrevious = previousNode
#             while tempPrevious.right:
#                 tempPrevious = tempPrevious.right
#             tempPrevious.right = root
#             root.left = None
#
#         return previousNode or root
#
#     # O(1) time / O(1) space
#     def next(self):
#         self.current = self.current.right
#         return self.current.val
#
#     # O(1) time / O(1) space
#     def hasNext(self):
#         return self.current.right is not None


class BSTIterator(object):
    # Solution 2
    # O(n) time / O(n) space
    def __init__(self, root):
        self.stack = []
        self.dfs(root)

    def dfs(self, root):
        while root is not None:
            self.stack.append(root)
            root = root.left

    # O(1) time / O(h) space
    def next(self):
        current = self.stack.pop()
        if current.right:
            self.dfs(current.right)

        return current.val

    # O(1) time / O(1) space
    def hasNext(self):
        return self.stack != []
