class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        results = set()
        while True:
            n = sum([int(i)**2 for i in str(n)])

            if n == 1:
                return True
            if n in results:
                return False
            results.add(n)


for num in xrange(10):
    print Solution().isHappy(num)




for i in xrange(10):
    continue
    print i**2

for i in xrange(100):
    continue
    print '%i: %s' % (i, Solution().isHappy(i))