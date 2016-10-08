

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroes = []
        for i in xrange(len(nums)):
            if nums[i] == 0:
                zeroes.append(i)
        for i in xrange(len(zeroes)):
            del nums[zeroes[i]-i]
            nums.append(0)

# print("\n".join(dir([])))
# print("\n".join(dir({1})))
print("\n".join(dir({1: 2})))

st = {1, 2, 3}
st = set([1,2,3])
st.pop()
lt = [4,2,4,0,0,3,0,5,1,0]
Solution().moveZeroes(lt)
print lt


nums = [4,2,4,0,0,3,0,5,1,0]
dt = dict()
for i in xrange(len(nums)):
    num = nums[i]
    dt[num] = 0 if num not in dt else dt[num]+1
print list(dt.viewkeys())[-1]


# eof
