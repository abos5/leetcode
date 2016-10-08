# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        it only works when it's the end
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        total = 0

        def travel(node, total):
            total += node.val
            if node.left and travel(node.left, total):
                return True
            elif node.right and travel(node.right, total):
                return True
            if not node.left and not node.right and total == sum:
                return True
            return False

        if not root:
            return False

        return travel(root, 0)


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        try loop instead of recursive calls
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        total = 0
        if not root:
            return False
        lt = []


        return travel(root, 0)


testCases = [
    (([1, 1, 0], 1), True),
    (([1], 1), True),
    (([[1, 2, 3, 4, 5, 7, 6], 7]), True),
    (([1, 2, 3, 4, 5, 7, 6, 1, 2, 2, 3, 4, 5, 6], 8), True),
    (([1, 2], 1), False),
    (([], 0), False)

]


# eof
