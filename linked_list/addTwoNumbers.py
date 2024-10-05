# https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # Solution 1
    # O(n) time / O(n) space
    def addTwoNumbers(self, l1, l2):
        num1, num2 = "", ""
        while l1 is not None:
            num1 += str(l1.val)
            l1 = l1.next

        while l2 is not None:
            num2 += str(l2.val)
            l2 = l2.next

        result = str(int(num1[::-1]) + int(num2[::-1]))
        head = ListNode(int(result[-1]), None)
        temp = head
        for val in reversed(result[:len(result) - 1]):
            nextNode = ListNode(int(val), None)
            temp.next = nextNode
            temp = temp.next

        return head
