# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def removeNthFromEnd(self, head, n):
        dummyHead = ListNode(0, head)
        beforeNthNode = dummyHead

        index = 0
        while head is not None:
            if index >= n:
                beforeNthNode = beforeNthNode.next
            head = head.next
            index += 1

        nodeToremove = beforeNthNode.next
        beforeNthNode.next = nodeToremove.next
        nodeToremove.next = None

        return dummyHead.next