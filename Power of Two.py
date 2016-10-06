class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while not n % 2:
            n = n / 2
        return n == 1

    def isPowerOf(self, n, base):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while not n % base:
            n = n / base
        return n == 1

for i in xrange(1025):
    rs = Solution().isPowerOf(i, 7)
    if rs:
        print(i, rs)