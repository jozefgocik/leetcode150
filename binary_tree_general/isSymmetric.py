# https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n) time / O(d) space
    # def isSymmetric(self, root):
    #     return self.isSymmetricHelper(root.left, root.right)
    #
    # def isSymmetricHelper(self, left, right):
    #     if left is None and right is None:
    #         return True
    #     elif left and right and left.val == right.val:
    #         return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)
    #     else:
    #         return False

    # Solution 2
    # O(n) time / O(n) space
    def isSymmetric(self, root):
        queue = [(root, root)]

        while queue:
            left, right = queue.pop(0)
            if not left and not right:
                continue
            elif left and right and left.val == right.val:
                queue.append([left.left, right.right])
                queue.append([left.right, right.left])
            else:
                return False

        return True
