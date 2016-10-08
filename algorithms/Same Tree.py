# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def depthFirst(p, q):
            if p is None:
                if q is None:
                    return True
                return False
            if q is None:
                return False
            if p.val != q.val:
                return False

            rs = depthFirst(p.left, q.left)
            if rs:
                return depthFirst(p.right, q.right)
            return False
        return depthFirst(p, q)


class Solution1(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None:
            if q is None:
                return True
            return False
        if q is None:
            return False
        if p.val != q.val:
            return False

        rs = self.isSameTree(p.left, q.left)
        if rs:
            return self.isSameTree(p.right, q.right)
        return False


class Solution2(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pn = p
        qn = q
        while True:
            if pn is None:
                if qn is None:
                    return True
                return False
            if qn is None:
                return False
            if pn.val != qn.val:
                return False
            pn = pn.left
            qn = qn.left
            continue

        rs = self.isSameTree(p.left, q.left)
        if rs:
            return self.isSameTree(p.right, q.right)
        return False


#eof
