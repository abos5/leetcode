class Solution(object):
    def canWinNim(self, n):
        """
        : rtype: bool
        """
        return n%4 != 0




s = Solution()
for i in range(10):
    print(i, s.canWinNim(i))
#eof
