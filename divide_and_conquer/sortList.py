# https://leetcode.com/problems/sort-list/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # Solution 1
    # O(n * log(n)) time / O(log(n)) space
    def sortList(self, head):
        if not head or head.next is None:
            return head

        slow, fast = ListNode(-1, head), head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(temp)

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
