# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        nth = length - n
        if nth == 0:
            return head.next
        temp = head
        for i in range(nth-1):
            temp = temp.next
        temp.next = temp.next.next
        return head
