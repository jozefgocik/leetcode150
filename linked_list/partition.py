# https://leetcode.com/problems/partition-list/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def partition(self, head, x):
    #     dummyHead = ListNode()
    #     currentHead = dummyHead
    #     dummyTail = ListNode()
    #     currentTail = dummyTail
    #
    #     while head is not None:
    #         if head.val < x:
    #             currentHead.next = ListNode(head.val)
    #             currentHead = currentHead.next
    #         else:
    #             currentTail.next = ListNode(head.val)
    #             currentTail = currentTail.next
    #         head = head.next
    #
    #     currentHead.next = dummyTail.next
    #
    #     return dummyHead.next

    # Solution 2
    # O(n) time / O(1) space
    def partition(self, head, x):
        dummyHead, dummyTail = ListNode(), ListNode()
        currentHead, currentTail = dummyHead, dummyTail

        while head is not None:
            tempNext = head.next
            head.next = None
            if head.val < x:
                currentHead.next = head
                currentHead = currentHead.next
            else:
                currentTail.next = head
                currentTail = currentTail.next
            head = tempNext

        currentHead.next = dummyTail.next

        return dummyHead.next
