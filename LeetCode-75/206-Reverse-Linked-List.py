# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head:ListNode):
        last = None
        while head:
            next = head.next
            head.next = last
            last = head
            head = next
        return last

        