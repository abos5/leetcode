class Solution(object):
    nfacs = {(2, 1): 2}

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if not rowIndex:
            return [1]

        middle = rowIndex // 2
        odd = rowIndex % 2
        line = [0] * (rowIndex + 1)
        line[0] = 1
        line[-1] = 1
        for i in xrange(1, middle + 1):
            f = self.nfac(rowIndex, i)
            line[i] = f
            line[-i-1] = f
        if not odd:  # index not odd then length odd
            line[middle] = self.nfac(rowIndex, middle)
        return line

    def nfac(self, rowIndex, i):
        """
        rowIndex >= 3
        i >= 1 item index
        """
        index = (rowIndex, i)
        if rowIndex == 1:
            return 1
        elif i == 1:
            return rowIndex
        elif index in self.nfacs:
            return self.nfacs[index]
        else:
            total = 0
            i1 = i - 1
            while rowIndex >= i:
                rowIndex = rowIndex - 1
                total += self.nfac(rowIndex, i1)
            self.nfacs[index] = total
            return total


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
         [1,3,3,1],
        [1,4,6,4,1],
       [1,5,10,10,5,1],
      [1,6,15,20,15,6,1],
     [1,7,21,35,35,21,7,1],
    [1,8,28,56,70,56,28,8,1],
   [1,9,36,84,126,126,84,36,9,1],
  [1,10,45,120,210,252,210,120,45,10,1],
 [1,11,55,165,330,462,462,330,165,55,11,1],
]


# line[n][2] = line[n-1][1] + line[n-2][1] ... line[1][1]
# line[n][i] = line[n-1][i-1] + line[n-2][i-1] ... line[1][i-1]



#eof
