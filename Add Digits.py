class Solution(object):
    def canWinNim(self, n):
        """
        : rtype: int
        """
        return 0 if not num else (num % 9 or 9)
        return (num % 9 or 9) if num else 0


def rough(num):
    return 0 if not num else (num%9 or 9)
    l = list(str(num))
    total = reduce(lambda a, b: int(a) + int(b), l)
    if len(str(total)) >= 2:
        total = rough(total)
    return int(total)


for i in range(200):
    print rough(i)
    continue
    if rough(i) != i%9:
        print i, ':', rough(i), i%9





#eof