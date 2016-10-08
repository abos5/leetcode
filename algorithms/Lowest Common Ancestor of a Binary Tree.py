# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    ancestor = None
    p = None
    q = None

    def lowestCommonAncestor(self, root, p, q):
        """
        valid the same node by p == q
        assuming there the ancestor always exists
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.p = p
        self.q = q
        self.ancestor = root
        self.markAncestor(root)
        return self.ancestor

    def markAncestor(self, node):

        if node.left and self.markAncestor(node.left):
                return self.ancestor
        if node.right and self.markAncestor(node.right):
                return self.ancestor

        if containsNode(node, self.p) and containsNode(node, self.q):
            self.ancestor = node
            return True

        return False


def containsNode(a, b):
    if a == b:
        return True
    if a.left and containsNode(a.left, b):
        return True
    if a.right and containsNode(a.right, b):
        return True
    return False


class Solution3(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        valid is same node by p == q
        a clean version of Solution1
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestor = findAncestor(root, p, q)
        return ancestor if ancestor else root


def findAncestor(node, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: mixed TreeNode if found else None
    """
    if not node:
        return False

    if node.left:
        found = findAncestor(node.left, p, q)
        if found:
            return found
    if node.right:
        found = findAncestor(node.right, p, q)
        if found:
            return found

    if containsNode(node, p) and containsNode(node, q):
        return node

    return False


def containsNode(a, b):
    if a == b:
        return True
    if a.left and containsNode(a.left, b):
        return True
    if a.right and containsNode(a.right, b):
        return True
    return False


# eof
