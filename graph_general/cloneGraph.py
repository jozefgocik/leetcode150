# https://leetcode.com/problems/clone-graph/?envType=study-plan-v2&envId=top-interview-150

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def cloneGraph(self, node):
        if not node:
            return None

        nodes = {}

        def dfs(current):
            if current.val in nodes:
                return
            currentCopy = Node(current.val)
            nodes[current.val] = currentCopy
            for neighbor in current.neighbors:
                dfs(neighbor)
                currentCopy.neighbors.append(nodes[neighbor.val])

        dfs(node)
        return nodes[1]
