class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        bases = [2, 3, 5, 6, 15, 90]
        for base in bases:
            # inspired by is power of two
            # then is power of any int
            while not num % base:
                num = num / base
            if num == 1:
                return True
        return False

for i in xrange(1025):
    rs = Solution().isUgly(i)
    if rs:
        print(i, rs)





#eof
