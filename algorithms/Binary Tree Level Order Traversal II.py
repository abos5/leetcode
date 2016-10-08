# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        okay 56ms 80%
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.lt = []
        self.traverse(root, 0)
        self.lt.reverse()
        return self.lt

    def traverse(self, node, level):
        if not node:
            return None
        if len(self.lt) == level:
            self.lt.append([])
        self.traverse(node.left, level+1)
        self.traverse(node.right, level+1)
        self.lt[level].append(node.val)


class Solution1(object):
    def levelOrderBottom(self, root):
        """
        nice 52ms 91%
        Using if before calling a function
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.lt = []
        if not root:
            return None
        self.traverse(root, 0)
        self.lt.reverse()
        return self.lt

    def traverse(self, node, level):
        if len(self.lt) == level:
            self.lt.append([])
        self.lt[level].append(node.val)
        if node.left:
            self.traverse(node.left, level+1)
        if node.right:
            self.traverse(node.right, level+1)



# print Solution().levelOrderBottom()
#eof
