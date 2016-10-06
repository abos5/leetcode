"""
failed to understand what
implementing queue using stacks means
Let's take another test round

Error 1: Used LinkedList to implement Stack
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.prev = None


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        Error 1: Used LinkedList to implement Stack
        """
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.size += 1
        node = ListNode(x)
        if self.size == 1:
            self.head = node
            self.tail = node
            return
        if self.size == 2:
            self.tail.prev = self.head
        node.prev, self.tail = self.tail, node

    def pop(self):
        """
        pop require adding the popped val to the head
        :rtype: nothing
        """
        if self.size == 0:
            return
        self.size -= 1
        val = self.tail.val
        if self.size == 0:
            self.head = None
            self.tail = None
            return val

        self.tail = self.tail.prev
        return val

    def peek(self):
        """
        peek means getting the head
        :rtype: int
        """
        if self.size == 0:
            return
        return self.head.val

    def empty(self):
        """
        :rtype: bool
        """
        return not self.size


class Queue1(object):
    def __init__(self):
        """
        @copyright from Discussion
        initialize your data structure here.
        early in later out so early out OUT
        later in early out so later out OUT
        """
        self.IN, self.OUT = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.IN.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.orginize()
        return self.OUT.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.orginize()
        return self.OUT[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.IN or self.OUT)

    def orginize(self):
        if not self.OUT:
            while self.IN:
                self.OUT.append(self.IN.pop())


q = Queue1()
q.push(1)
q.push(2)
# q.push(3)
print q.pop() # 1
q.push(4)
q.push(5)
# q.push(6)
print q.peek()
print q.pop()
print '====='
q = Queue1()
q.push(1)

# test case 0
q = Queue1()
q.push(1)
q.push(2)
q.pop()
print q.peek() == 2
print '========'
# test case 1
q = Queue1()
q.push(1)
q.push(2)
print q.peek() == 1
print '========'
# test case 2
q = Queue1()
q.push(1)
q.push(2)
q.pop()
q.push(3)
q.push(4)
q.pop()
print q.peek() == 3
print '========='
# for i in xrange(10):
#     q.push(i)

# q.push(None)

while not q.empty():
    print q.pop()

#eof



