#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        node = head
        while node is not None:
            l.append(node.val)
            node = node.next
        middle = len(l) // 2
        linked_list = ListNode()
        next_node = linked_list
        for x in l[middle:]:
            next_node.val = x
            next_node = next_node.next
        return linked_list