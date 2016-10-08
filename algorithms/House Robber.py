class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t0, t1 = 0, 0
        for i, item in enumerate(nums):
            if i % 2:
                t0 += item
            else:
                t1 += item
        return t0 if t0 > t1 else t1


testCases = [
    ([2, 1, 1, 2], 4),
    ([2, 1, 1, 2], 4),
    ([1, 1, 2, 2, 3, 4, 5, 5], 12),
    ([1, 1, 2, 2, 3, 4, 5, 5, 99], 110),
    ([1], 1),
    ([], 0),
]

for c, expect in testCases:
    print expect == Solution().rob(c)

