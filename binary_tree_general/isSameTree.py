# https://leetcode.com/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def isSameTree(self, p, q):
    #     queueP = [p]
    #     queueQ = [q]
    #
    #     while queueP and queueQ:
    #         currentP = queueP.pop(0)
    #         currentQ = queueQ.pop(0)
    #         if currentP is not None and currentQ is not None and currentP.val == currentQ.val:
    #             queueP.append(currentP.left)
    #             queueP.append(currentP.right)
    #             queueQ.append(currentQ.left)
    #             queueQ.append(currentQ.right)
    #         elif currentP != currentQ:
    #             return False
    #
    #     return True

    # Solution 2
    # O(n) time / O(d) space; d = depth
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is not None and q is not None and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
