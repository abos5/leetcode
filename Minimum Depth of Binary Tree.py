# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        be ware of the Definition of Leaf
        :type root: TreeNode
        :rtype: int
        """
        level = [root]
        i = 0
        while root and level:
            i += 1
            for n in level:
                if not n.left and not n.right:
                    return i
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return i


class Solution1(object):
    def minDepth(self, root):
        """
        be ware of the Definition of Leaf
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lvl = [root]
        i = 1
        while True:
            for n in lvl:
                if not n.left and not n.right:
                    return i
            lvl, i = [k for n in lvl for k in (n.left, n.right) if k], i + 1


class Solution1(object):
    def minDepth(self, root):
        """
        use Space(n) to decrease one O(n)

        conclusion: Space(n) is slower than O(n)
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lvl = [root]
        i = 1
        tmp = []
        while True:
            for n in lvl:
                if not n.left and not n.right:
                    return i
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            lvl, i, tmp = tmp, i + 1, []

print 2 << 0
print 2 << 1

# testCases
# [1,2,2,3,3,3,3,4,4,4,5,4,5]
# [1,2,2,3,3,3,3,4,4,null,5,null,5] 3
# [1,null,2,null,3]  3
# [1,2,2,null,3]     2
# [1, null, null]  1
# [1,null,1]  2
# [1,2,2,3,3,null,4,4,4,null,5,6,7,8,9,null]   4

#eof
