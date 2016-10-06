#! /bin/sh
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution0(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDepth = 0

        def TravelInOrder(node, height):
            if node is None:
                return
            height += 1
            if height > self.maxDepth:
                self.maxDepth = height
            TravelInOrder(node.left, height)
            TravelInOrder(node.right, height)
        TravelInOrder(root, 0)
        return self.maxDepth


class Solution1(object):
    def maxDepth(self, root, height=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if height == 0:
            self.max = 0

        if root is None:
            return self.max
        height += 1
        if height > self.max:
            self.max = height
        self.maxDepth(root.left, height)
        self.maxDepth(root.right, height)
        return self.max


class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDepth = 0

        def TravelInOrder(node, height):
            if height == 0 and node is None:
                return
            height += 1
            if height > self.maxDepth:
                self.maxDepth = height

            if node.left is not None:
                TravelInOrder(node.left, height)
            if node.right is not None:
                TravelInOrder(node.right, height)
        TravelInOrder(root, 0)
        return self.maxDepth

#eof
