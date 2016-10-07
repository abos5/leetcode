"""
Time Limit Exceeded
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in xrange(0, l):
            for j in xrange(0, l):
                if i == j:
                    continue
                s = nums[i] + nums[j]
                if target == s:
                    return [i, j]
        return None


# eof
