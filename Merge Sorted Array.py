class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l1 = len(nums1)
        j = 0
        for n2 in nums2:
            if n2 < nums1[j]:
                nums1.insert(j, n2)
            j += 1




slu = Solution()
lt = [1, 3, 5]
slu.merge(lt, 3, [2, 4, 6], 2)
print lt



#eof
