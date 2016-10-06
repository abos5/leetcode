class Solution(object):
    def removeDuplicates(self, nums):
        """
        bad 136ms 22.7%
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = 1
        while True:
            if len(nums) == l:
                return l
            elif nums[l-1] == nums[l]:
                del nums[l]
            else:
                l += 1
        #


class Solution0(object):
    def removeDuplicates(self, nums):
        """
        no remove here
        DAMN got fooled in Discussion Board
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        c = -1
        last = None
        for i, item in enumerate(nums):
            if last == item:
                c += 1
            else:
                last = item
        return i - c


class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last = None
        deleted = 0
        for i, item in enumerate(nums):
            print i, last, item, nums[i-deleted], deleted
            if item == last:
                del nums[i-deleted]
                deleted += 1
                continue
            last = item
        return i - deleted


class Solution2(object):
    def removeDuplicates(self, nums):
        """
        bad 144ms 18.4%
        middle term deletion
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = 1
        while True:
            ln = len(nums)
            if ln == l:
                return l
            elif nums[l-1] == nums[l]:
                if l < ln//2:
                    del nums[l]
                else:
                    nums.pop(l)
            else:
                l += 1
        return l

testCases = [
    [1, 1, 2, 2, 3, 4, 5, 5],
    [1, 1, 2, 2, 3, 4, 5, 5, 99],
    [2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8],
    [1],
]

for c in testCases:
    print Solution0().removeDuplicates(c)

for c in testCases:
    Solution2().removeDuplicates(c)

print testCases
# print "\n".join(testCases)

#eof
