# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # Solution 1
    # O(n) time / O(d) space
    # def maxDepth(self, root):
    #     return self.maxDepthHelper(root, 0, 0)
    #
    # def maxDepthHelper(self, root, depth, maxDepth):
    #     if root is None:
    #         return max(maxDepth, depth)
    #
    #     maxDepth = max(maxDepth, self.maxDepthHelper(root.left, depth + 1, maxDepth))
    #     maxDepth = max(maxDepth, self.maxDepthHelper(root.right, depth + 1, maxDepth))
    #
    #     return maxDepth

    # Solution 2
    # O(n) time / O(d) space
    # def maxDepth(self, root):
    #     if not root:
    #         return 0
    #
    #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # Solution 3
    # O(n) time / O(n) space
    def maxDepth(self, root):
        result = 0
        queue = [[root, 1]]
        while queue:
            node, level = queue.pop(0)
            if node:
                queue.append([node.left, level + 1])
                queue.append([node.right, level + 1])
                result = max(result, level)

        return result


