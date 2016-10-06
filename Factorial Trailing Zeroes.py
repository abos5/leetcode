class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            c, n = c + n // 5, n // 5
        return c


slu = Solution()
# slu1 = Solution1()
for i in xrange(1, 1, 1):
    print slu.trailingZeroes(i), i
print slu.trailingZeroes(113), 110


testCases = [
    (11, 2),
    (110, 26),
    (113, 26),
    (114, 26),
    (18, 3),
    (19, 3),
    (10, 2),
    (9, 1),
    (0, 0),
    (200, 49),
    (199, 47),
    (124, 28),
    (125, 31),
    (249, 59),
    (250, 62),
    (624, 152),
    (625, 156),
    (724, 178),
    (725, 180),
]

for case, expect in testCases:
    print case, expect, slu.trailingZeroes(case), slu.trailingZeroes(case) == expect


#eof
