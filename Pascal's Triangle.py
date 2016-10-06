class Solution(object):
    facs = [0]
    nfacs = {(2, 1): 2}

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        elif numRows == 1:
            return [[1]]
        lt = [[1], [1, 1]]

        for l in xrange(2, numRows):
            middle = l // 2
            odd = l % 2
            line = [0] * (l + 1)
            line[0] = 1
            line[-1] = 1
            for i in xrange(1, middle + 1):
                f = self.nfac(l, i)
                line[i] = f
                line[-i-1] = f
            if not odd:  # index not odd then length odd
                line[middle] = self.nfac(l, middle)
            lt += [line]
        return lt

    def nfac(self, l, i):
        """
        l >= 3
        i >= 1
        """
        index = (l, i)
        if l == 1:
            return 1
        elif i == 1:
            return l
        elif index in self.nfacs:
            return self.nfacs[index]
        else:
            total = 0
            i1 = i - 1
            while l >= i:
                l = l - 1
                total += self.nfac(l, i1)
            self.nfacs[index] = total
            return total


class Solution(object):
    res = [[1]]

    def generate(self, numRows):
        """
        copy from discussion and add 'if numRows else []' to the tail.
        Explanation:
        Any row can be constructed using the offset sum of the previous row.
        Example:
            1 3 3 1 0
         +  0 1 3 3 1
         =  1 4 6 4 1
        """
        for i in range(len(self.res), numRows):
            self.res += [map(lambda a, b: a + b, self.res[-1] + [0], [0] + self.res[-1])]
        return self.res[:numRows]


slu = Solution()
try:
    rs = slu.generate(10)
except RuntimeError, e:
    rs = [[]]
print rs
print slu.generate(10)

testCases = [
    (10, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1]])
]

[
            [1],
           [1,1],
          [1,2,1],
         [1,3,3,  1],
        [1,4,6,  4,1],
       [1,5,10, 10,5,1],
      [1,6,15, 20,15,6,1],
     [1,7,21, 35,35,21,7,1],
    [1,8,28, 56,70,56,28,8,1],
   [1,9,36, 84,126,126,84,36,9,1],
  [1,10,45,120,210,252,210,120,45,10,1],
 [1,11,55,165,330,462,462,330,165,55,11,1],
]


# line[n][2] = line[n-1][1] + line[n-2][1] ... line[1][1]
# line[n][i] = line[n-1][i-1] + line[n-2][i-1] ... line[1][i-1]

# (9, 4) = (8, 3) + (7, 3) + (6, 3) ... (3, 3)
#        = (7, 2) + (6, 2) + ... (2, 2) + (7, 3) + (6, 3) ... + (3, 3)
#        = 1 +

# (5, 3) = (4, 2) + (3, 2) + (2, 2)
#        = (3, 1) + (2, 1) + (1, 1) + (2, 1) + (1, 1) + (2, 2)
#        = (2, 0) + (1, 0) + (0, 0) + (1, 0) + (0, 0) + (1, 1) + (1, 0) + (0, 0) + (1, 1) + (2, 2)
#        = 10




#eof
