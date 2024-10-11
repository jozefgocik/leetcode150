# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def deleteDuplicates(self, head):
    #     dummyHead = ListNode()
    #     currentNode = dummyHead
    #
    #     while head is not None:
    #         tempHead = head
    #         while head is not None and head.val == tempHead.val:
    #             head = head.next
    #
    #         if tempHead.next == head:
    #             currentNode.next = ListNode(tempHead.val)
    #             currentNode = currentNode.next
    #
    #     return dummyHead.next

    # Solution 2
    # O(n) time / O(1) space
    def deleteDuplicates(self, head):
        dummyHead = ListNode()
        currentNode = dummyHead

        while head is not None:
            tempHead = head
            while head is not None and head.val == tempHead.val:
                head = head.next

            if tempHead.next == head:
                currentNode.next = tempHead
                currentNode = currentNode.next
                currentNode.next = None

        return dummyHead.next
