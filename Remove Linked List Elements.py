# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None

        # make sure head.val != val and head is not None
        while head.val == val:
            if head.next is None:
                return None
            head = head.next

        cNode = head
        while cNode.next is not None:
            if cNode.next.val == val:
                cNode.next = cNode.next.next
            else:
                cNode = cNode.next

        return head


#eof
