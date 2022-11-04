# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def palindrome(self, lista):
        i = 0
        j = len(lista) - 1
        while lista[i] == lista[j] and i < j:
            i += 1
            j -= 1
        return i >= j

    def isPalindrome(self, head):
        lista = []
        while head != None:
            lista.append(head.val)
            head = head.next
        return self.palindrome(lista)
    
s = Solution()
print(s.palindrome([1,2,1]))