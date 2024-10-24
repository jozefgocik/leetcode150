# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/?envType=study-plan-v2&envId=top-interview-150

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def connect(self, root):
        queue = [root]
        while queue:
            nextQueue = []
            while queue:
                current = queue.pop(0)
                if current:
                    if queue:
                        current.next = queue[0]
                    if current.left:
                        nextQueue.append(current.left)
                    if current.right:
                        nextQueue.append(current.right)

            queue = nextQueue

        return root
