import random


class Solution(object):
    def isAnagram(self, s, t):
        """
        O(6n)
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        l_s = len(s)
        l_t = len(t)
        if l_s != l_t:
            return False
        sl = [ord(i) for i in s]
        tl = [ord(i) for i in t]
        sum_s = sum(sl)
        sum_t = sum(tl)
        pro_s = reduce(lambda a, b: a*b, sl)
        pro_t = reduce(lambda a, b: a*b, tl)

        return sum_s == sum_t and pro_s == pro_t


class Solution1(object):
    def isAnagram(self, s, t):
        """
        O(3n)
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        l_s = len(s)
        l_t = len(t)
        if l_s != l_t:
            return False
        lt = [0]*26
        for i in xrange(l_s):
            lt[ord(s[i])-97] += 1
            lt[ord(t[i])-97] -= 1
        for i in lt:
            if i:
                return False
        return True


class Solution2(object):
    def isAnagram(self, s, t):
        """
        Does s equal t?
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        list_s = [0]*26
        list_t = [0]*26

        for ch in s:
            list_s[ord(ch)-97] += 1
        for ch in t:
            list_t[ord(ch)-97] += 1

        return list_s == list_t


i = random.randint(1, 1000000)
# print list_s
print Solution1().isAnagram('abc', 'acb')
print Solution1().isAnagram('', '')
print Solution1().isAnagram('abcdef', 'abedef')

