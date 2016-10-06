class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        strs.sort()
        common = strs[0]
        while common:
            l = len(common)
            for s in strs:
                if common != s[:l]:
                    break
            else:
                break
            common = common[:l]
        return common


class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        trying dichotomy
        fucking failed @date(2015-11-03)
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        common = strs[0]
        big = len(strs[0])
        small = 0
        middle = big//2
        while common:
            for s in strs:
                if common != s[:middle]:
                    break
            else:
                # ok, increse middle
                middle, small = (big + middle) // 2, middle
                if middle == small:  # match
                    break
                continue
            # not ok, decrese middle
            middle, big = (small + middle) // 2, middle
            common = common[:middle]

        return common

class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        without sort
        find shortest str during matching
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        i = 0
        p = 0
        common = strs[i][:p]
        while common:
            for s in strs:
                if common != s[:p]:
                    break
            else:
                common = strs[i][:p+1]
                continue
            break
        return common

# test case:
# test case:
# test case:
# test case:
testCases = [
    ["123123"],
    ["123123","123124"],
    ["123123","1231"],
    ["123123","123123"],
]
for c in testCases:
    Solution2().longestCommonPrefix(c)

#eof
