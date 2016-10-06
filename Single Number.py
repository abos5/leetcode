class Solution(object):
    def singleNumber(self, nums):
        """
        learnt bit operations from discussion
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda a, b: a ^ b, nums)
def decbin(num):
    if not num:
        return 0
    lt = []
    while num > 1:
        left = num % 2
        lt.append(left)
        num //= 2

    lt.append(1)
    total = 0
    for i, item in enumerate(lt):
        total += item * (10 ** i)
    return total

def b_not(a, b):
    return decbin(a), decbin(b), a ^ b

def b_or(a, b):
    return decbin(a), decbin(b), a | b

def b_and(a, b):
    return decbin(a), decbin(b), a & b



print b_and(9, 100)
print b_or(9, 100)
print b_or(9, 9)
print b_not(9, 100)
print b_not(100, 9)
print b_not(9, 0)
print b_not(9, 10)
print b_not(9, 6), decbin(15)

print 1 | 2 | 3 | 4
print 4 | 3 | 1 | 2




#eof
