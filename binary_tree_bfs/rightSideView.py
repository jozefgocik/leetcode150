# https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # Solution 1
    # O(n) time / O(n) space
    def rightSideView(self, root):
        result = []
        if not root:
            return result

        queue = [root]
        while queue:
            result.append(queue[-1].val)
            tempQueue = []
            while queue:
                current = queue.pop(0)
                if current.left:
                    tempQueue.append(current.left)
                if current.right:
                    tempQueue.append(current.right)
            queue = tempQueue

        return result
