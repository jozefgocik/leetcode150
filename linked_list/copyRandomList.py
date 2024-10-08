# https://leetcode.com/problems/copy-list-with-random-pointer/?envType=study-plan-v2&envId=top-interview-150

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def copyRandomList(self, head):
    #     cache = {None: None}
    #     dummyHead = Node(0)
    #
    #     newListPointer = dummyHead
    #     oldListPointer = head
    #     while oldListPointer is not None:
    #         newNode = Node(oldListPointer.val)
    #         cache[oldListPointer] = newNode
    #         newListPointer.next = newNode
    #         newListPointer = newListPointer.next
    #         oldListPointer = oldListPointer.next
    #
    #     newListPointer = dummyHead.next
    #     oldListPointer = head
    #     while oldListPointer is not None:
    #         newListPointer.random = cache[oldListPointer.random]
    #         newListPointer = newListPointer.next
    #         oldListPointer = oldListPointer.next
    #
    #     return dummyHead.next

    # Solution 2
    # O(n) time / O(n) space
    def copyRandomList(self, head):
        cache = {None: None}

        current = head
        while current:
            newNode = Node(current.val)
            cache[current] = newNode
            current = current.next

        current = head
        while current:
            newNode = cache[current]
            newNode.next = cache[current.next]
            newNode.random = cache[current.random]
            current = current.next

        return cache[head]
