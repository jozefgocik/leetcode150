# https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    # def mergeTwoLists(self, list1, list2):
    #     head = None
    #     currentNode = head
    #     while list1 is not None and list2 is not None:
    #         nextNode = ListNode(list1.val, None) if list1.val < list2.val else ListNode(list2.val, None)
    #         if currentNode is None:
    #             head = nextNode
    #             currentNode = nextNode
    #         else:
    #             currentNode.next = nextNode
    #             currentNode = currentNode.next
    #
    #         if list1.val < list2.val:
    #             list1 = list1.next
    #         else:
    #             list2 = list2.next
    #
    #     if list1 is not None:
    #         if currentNode is None:
    #             head = list1
    #             currentNode = list1
    #         else:
    #             currentNode.next = list1
    #     elif list2 is not None:
    #         if currentNode is None:
    #             head = list2
    #             currentNode = list2
    #         else:
    #             currentNode.next = list2
    #
    #     return head

    # Solution 2
    # O(n) time / O(1) space
    def mergeTwoLists(self, list1, list2):
        dummyHead = ListNode()
        currentNode = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                currentNode.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                currentNode.next = ListNode(list2.val, None)
                list2 = list2.next
            currentNode = currentNode.next

        if list1:
            currentNode.next = list1
        elif list2:
            currentNode.next = list2

        return dummyHead.next