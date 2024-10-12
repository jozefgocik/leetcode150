# https://leetcode.com/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(1) space
    # def rotateRight(self, head, k):
    #     length = self.getLength(head)
    #     if length <= 1:
    #         return head
    #
    #     k = k % length
    #     temp = head
    #     while k > 0:
    #         nodeBeforeTail = None
    #         while temp.next is not None:
    #             nodeBeforeTail = temp
    #             temp = temp.next
    #
    #         newHead = nodeBeforeTail.next
    #         nodeBeforeTail.next = None
    #         newHead.next = head
    #         head = newHead
    #         k -= 1
    #
    #     return head
    #
    # def getLength(self, head):
    #     length = 0
    #     while head is not None:
    #         head = head.next
    #         length += 1
    #
    #     return length

    # Solution 2
    # O(n) time / O(n) space
    # def rotateRight(self, head, k):
    #     length = self.getLength(head)
    #     if length <= 1:
    #         return head
    #
    #     k = k % length
    #     cache = {}
    #     for i in range(length):
    #         index = (i + k) % length
    #         cache[index] = ListNode(head.val)
    #         head = head.next
    #
    #     dummyHead = ListNode()
    #     currentNode = dummyHead
    #     for i in range(length):
    #         currentNode.next = cache[i]
    #         currentNode = currentNode.next
    #
    #     return dummyHead.next
    #
    # def getLength(self, head):
    #     length = 0
    #     while head is not None:
    #         head = head.next
    #         length += 1
    #
    #     return length

    # Solution 3
    # O(n) time / O(1) space
    def rotateRight(self, head, k):
        if not head:
            return head

        length, tail = 1, head
        while tail.next is not None:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        current = head
        for i in range(length - k - 1):
            current = current.next

        newHead = current.next
        current.next = None
        tail.next = head

        return newHead
