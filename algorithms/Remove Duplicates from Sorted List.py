# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from lib.list import ListNode
from lib.list import getHeadOfListNodeFromList


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = head
        while n and n.next:
            if n.next.val == n.val:
                n.next = n.next.next
            else:
                n = n.next
        return head

h = getHeadOfListNodeFromList([1,1,2,2,3,4,5,5])
h = getHeadOfListNodeFromList([1,1,2,2,3,4,5,5,99])
h = getHeadOfListNodeFromList([1,2,3,4,4,4,5,5,5,5,5,5,5,5,5,6,7,8])
h = getHeadOfListNodeFromList([1])
h = getHeadOfListNodeFromList([])

print Solution().deleteDuplicates(h)
