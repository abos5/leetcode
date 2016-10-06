

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        n = self
        lt = []
        while n:
            lt.append(n.val)
            n = n.next
        return unicode(lt)


def getHeadOfListNodeFromList(lt):
    h = ListNode(0)
    node = h
    for v in lt:
        node.next = ListNode(v)
        node = node.next

    return h.next

#eof
