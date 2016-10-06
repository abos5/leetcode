class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dt = dict()
        ln = len(nums)
        for i in range(ln):
            dt[nums[i]] = 1
        return ln != len(dt)


class Solution1(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        st = set()
        ln = len(nums)
        for i in xrange(ln):
            st.add(nums[i])
            if len(st) != (i+1):
                return True
        return False


class Solution2(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        st = set()
        ln = len(nums)
        for i in range(ln):
            st.add(nums[i])
        return ln != len(st)


class Solution3(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

st = set()
print st.add(1)
print st.add(1)
print("\n".join(dir([])))
s = Solution()
print(s.containsDuplicate([1,2,3,4,6]))
#eof
