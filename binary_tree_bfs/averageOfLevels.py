# https://leetcode.com/problems/average-of-levels-in-binary-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # Solution 1
    # O(n) time / O(n) space
    def averageOfLevels(self, root):
        result = []
        queue = [root]

        while queue:
            current = 0.0
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if node:
                    current += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(current/float(length))

        return result
