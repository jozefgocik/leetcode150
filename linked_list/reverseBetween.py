# https://leetcode.com/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def reverseBetween(self, head, left, right):
    #     dummyHead = ListNode()
    #     currentNode = dummyHead
    #
    #     i = 0
    #     while i < left - 1:
    #         nextNode = ListNode(head.val)
    #         currentNode.next = nextNode
    #         currentNode = currentNode.next
    #         head = head.next
    #         i += 1
    #
    #     dummyTail = ListNode(head.val)
    #     head = head.next
    #     currentTail = dummyTail
    #     while i < right - 1:
    #         previousNode = ListNode(head.val, currentTail)
    #         currentTail = previousNode
    #         head = head.next
    #         i += 1
    #
    #     dummyTail.next = head
    #     currentNode.next = currentTail
    #
    #     return dummyHead.next

    # Solution 2
    # O(n) time / O(1) space
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)

        leftPrevious, current = dummy, head
        for i in range(left - 1):
            leftPrevious = current
            current = current.next

        previousNode = None
        for i in range(right - left + 1):
            tempNext = current.next
            current.next = previousNode
            previousNode = current
            current = tempNext

        leftPrevious.next.next = current
        leftPrevious.next = previousNode

        return dummy.next
