

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s)
        return sum([(ord(s[i])-64)*(26**(l-i-1)) for i in range(l)])
        # test code
        return list([(ord(s[i])-64)*(26**(l-i-1)) for i in range(l)])



print Solution().titleToNumber('AZ')

#eof
