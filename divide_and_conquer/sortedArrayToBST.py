# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n) time / O(log(n)) space
    def sortedArrayToBST(self, nums):
        if not nums:
            return

        index = len(nums)//2
        root = TreeNode(nums[index])

        root.left = self.sortedArrayToBST(nums[0:index])
        root.right = self.sortedArrayToBST(nums[index+1:])

        return root
