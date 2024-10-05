# https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def hasCycle(self, head):
    #     seen = set()
    #     temp = head
    #     while temp is not None:
    #         if temp in seen:
    #             return True
    #         seen.add(temp)
    #         temp = temp.next
    #
    #     return False

    # Solution 2
    # O(n) time / O(1) space
    def hasCycle(self, head):
        slow, fast = head, head
        started = False
        while fast is not None and fast.next is not None:
            if started and slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next
            started = True

        return False
