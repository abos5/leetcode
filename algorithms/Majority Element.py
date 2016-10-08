class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dt = dict()
        for i in xrange(len(nums)):
            num = nums[i]
            dt[i] = set()
            j = 0
            for j in xrange(i):
                if num not in dt[j]:
                    dt[j].add(num)
                    break

        for i in reversed(xrange(len(dt))):
            if len(dt[i]) != 0:
                return dt[i].pop()


class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dt = dict()
        for i in xrange(len(nums)):
            num = nums[i]
            dt[num] = 1 if num not in dt else dt[num]+1
        m = 0
        v = 0
        for key, item in dt.items():
            if item > m:
                m = item
                v = key
        return v
lt = []
lt.insert(0, 1)
lt.insert(0, 2)
lt.insert(0, 3)
lt.insert(0, 2)
lt.insert(0, 2)
lt.insert(0, 2)

lt0 = [1]
lt1 = [2]
print(lt)
print("\n".join(dir(lt)))
rs = Solution1().majorityElement(lt)

print(rs)

#eof
