# https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n) time / O(d) space
    # def sumNumbers(self, root, currentNum="", totalSum=0):
    #     if not root:
    #         return 0
    #
    #     currentNum += str(root.val)
    #     if not root.left and not root.right:
    #         totalSum += int(currentNum)
    #         return totalSum
    #
    #     return self.sumNumbers(root.left, currentNum, totalSum) + self.sumNumbers(root.right, currentNum, totalSum)

    # Solution 2
    # O(n) time / O(d) space
    def sumNumbers(self, root, currentNum=0, totalSum=0):
        if not root:
            return 0

        currentNum = currentNum * 10 + root.val
        if not root.left and not root.right:
            totalSum += currentNum
            return totalSum

        return self.sumNumbers(root.left, currentNum, totalSum) + self.sumNumbers(root.right, currentNum, totalSum)
