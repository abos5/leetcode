from lib.list import ListNode
from lib.list import getHeadOfListNodeFromList


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        h = ListNode(0)
        pre = h
        while head.next:
            # find last node
            c = head
            while c:
                if not c.next:
                    pre.next = ListNode(c.val)
                    pre = pre.next
                    prepre.next = None
                elif not c.next.next:
                    prepre = c
                c = c.next
        pre.next = ListNode(head.val)
        return h.next


class Solution1(object):

    def reverseList(self, head):
        """
        bad 64ms 37%
        recursive way
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)

        self.getNextVal(head, h)
        return h.next

    def getNextVal(self, head, n):
        if head and head.next:
            n = self.getNextVal(head.next, n)
        if head:
            n.next = ListNode(head.val)
        return n.next

lt = getHeadOfListNodeFromList([1, 2, 3, 4])

rs = Solution1().reverseList(lt)
print(rs)

# eof
