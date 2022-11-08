class Solution(object):
    def removeNthFromEnd(self, head, n):
        pont_ini, pont_end = head, head
        for _ in range(n):
            pont_end = pont_end.next
        if not pont_end: return head.next
    
        while pont_end.next:
            pont_end, pont_ini = pont_end.next, pont_ini.next
        pont_ini.next = pont_ini.next.next
        return head