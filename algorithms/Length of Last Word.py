class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s)
        c = 0
        i = 1
        while l - i > -1:
            o = ord(s[-i])
            if 64 < o < 91 or 96 < o < 123:
                c += 1
            elif c != 0:
                break

            i += 1
        return c

class Solution1(object):
    def lengthOfLastWord(self, s):
        """
        if only space and chars
        :type s: str
        :rtype: int
        """
        l = len(s)
        c = 0
        i = 1
        while l - i > -1:
            if s[-i] != ' ':
                c += 1
            elif c != 0:
                break

            i += 1
        return c


s = ''
s = 'ab cd   aascasc '
l = len(s)
print Solution1().lengthOfLastWord(s)
#eof

