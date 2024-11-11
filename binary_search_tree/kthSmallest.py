# https://leetcode.com/problems/kth-smallest-element-in-a-bst/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def kthSmallest(self, root, k):
        return self.kthSmallestHelper(root, k, [])[k - 1]

    def kthSmallestHelper(self, root, k, array):
        if not root or len(array) >= k:
            return array

        self.kthSmallestHelper(root.left, k, array)
        array.append(root.val)
        self.kthSmallestHelper(root.right, k, array)

        return array
