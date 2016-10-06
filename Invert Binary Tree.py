# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Test Case:
# [1,2,3,4,5,null,6,7,null,8,9,0,11,12,null,13,null,14,15]


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        root.left, root.right = root.left, root.right
        return root


class Solution1(object):
    def invertTree(self, root):
        """
        direct call recursive without using if
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root


class Solution2(object):
    def invertTree(self, root):
        """
        swap first
        direct call recursive without using if
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class Solution3(object):
    def invertTree(self, root):
        """
        use 'not node' instead of 'node is None'
        use a function
        swap first
        direct call recursive without using if
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        swapNodes(root)
        return root


def swapNodes(node):
    if not node:
        return

    node.left, node.right = node.right, node.left
    swapNodes(node.left)
    swapNodes(node.right)


class Solution4(object):
    def invertTree(self, root):
        """
        use loop
        :type root: TreeNode
        :rtype: TreeNode
        """
        node = root
        while node:
            node.left, node.right = node.right, node.left
            curr = node
            if node.left:
                node = node.left
                continue
            if node.right:
                node = node.right
                continue

        return root

for x in xrange(10):
    for y in xrange(10):
        print x*y
        if x*y > 50:
            break
    else:
        continue  # executed if the loop ended normally (no break)
    break  # executed if 'continue' was skipped (break)

#eof
