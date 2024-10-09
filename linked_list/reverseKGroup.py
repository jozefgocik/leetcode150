# https://leetcode.com/problems/reverse-nodes-in-k-group/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def reverseKGroup(self, head, k):
        dummyHead = ListNode()
        currentNode = dummyHead

        while head is not None:
            currentHead = head
            i = 0
            while i < k:
                if head is None:
                    break
                else:
                    head = head.next
                    i += 1
            currentTail = head
            if i == k:
                currentNode.next = self.reverseKGroupHelper(currentHead, currentTail)
                while currentNode.next is not None:
                    currentNode = currentNode.next
            else:
                currentNode.next = currentHead

        return dummyHead.next

    def reverseKGroupHelper(self, head, tail):
        previousNode = None
        while head is not tail:
            tempNext = head.next
            head.next = previousNode
            previousNode = head
            head = tempNext

        return previousNode