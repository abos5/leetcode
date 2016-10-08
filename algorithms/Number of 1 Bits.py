class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        c = 1
        while n > 1:
            if n % 2:
                c += 1
            n = n // 2
        return c

def decbin(n):
    if n == 0:
        return 0
    c = 1
    rs = []
    while n > 1:
        if n % 2:
            c += 1
            rs.append('1')
        else:
            rs.append('0')
        n = n // 2
    rs.reverse()
    print '1%s' % ("".join(rs)),
    return c

for i in xrange(100):
    print '%i: %i' % (i, decbin(i))
# print Solution().hammingWeight(1)

# eof

