# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        bad 76 ms 19%
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        cNode = head
        while True:
            if l1 is None:
                cNode.next = l2
                break
            elif l2 is None:
                cNode.next = l1
                break
            elif l1.val <= l2.val:
                cNode.next = l1
                l1 = l1.next
            else:
                cNode.next = l2
                l2 = l2.next
            cNode = cNode.next

        return head


class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        okay 56 ms 83%
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val < l2.val:
            head, l1 = l1, l1.next
        else:
            head, l2 = l2, l2.next

        cNode = head
        while True:
            if l1 is None:
                cNode.next = l2
                break
            elif l2 is None:
                cNode.next = l1
                break
            elif l1.val < l2.val:
                cNode.next, l1 = l1, l1.next
            else:
                cNode.next, l2 = l2, l2.next
            cNode = cNode.next

        return head


class Solution2(object):
    def mergeTwoLists(self, l1, l2):
        """
        clear solution inspired by discuss
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)
        n = h
        while l1 and l2:
            if l1.val < l2.val:
                n.next, l1 = l1, l1.next
            else:
                n.next, l2 = l2, l2.next
            n = n.next
        if l1:
            n.next = l1
        if l2:
            n.next = l2
        return h.next


class Solution3(object):
    def mergeTwoLists(self, l1, l2):
        """
        clear solution copy from discuss
        without polluting original data l1 l2
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        p, p1, p2 = sentinel, l1, l2
        while p1 and p2:
            if p1.val < p2.val:
                p.next,p1 = p1, p1.next
            else:
                p.next,p2 = p2, p2.next
            p = p.next

        while p1:
            p.next, p1 = p1, p1.next
            p = p.next

        while p2:
            p.next, p2 = p2, p2.next
            p = p.next

        return sentinel.next

#eof
