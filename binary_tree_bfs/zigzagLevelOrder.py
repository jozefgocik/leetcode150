# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def zigzagLevelOrder(self, root):
        result = []
        if not root:
            return result

        queue = [root]
        isLeft = True
        while queue:
            current = []
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current.append(node.val)

            if isLeft:
                result.append(current)
            else:
                result.append(current[::-1])
            isLeft = not isLeft

        return result
