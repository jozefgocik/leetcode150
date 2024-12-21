# https://leetcode.com/problems/merge-k-sorted-lists/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # Solution 1
    # O(n * log(k)) time / O(1) space
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        n = len(lists) // 2
        left = self.mergeKLists(lists[0:n])
        right = self.mergeKLists(lists[n:])

        dummy = ListNode()
        current = dummy
        while left is not None and right is not None:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        if left is not None:
            current.next = left
        if right is not None:
            current.next = right

        return dummy.next
