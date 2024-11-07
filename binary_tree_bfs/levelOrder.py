# https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def levelOrder(self, root):
        result = []
        if not root:
            return result

        queue = [root]
        while queue:
            current = []
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                current.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current)

        return result
