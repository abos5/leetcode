# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        unfinished version by val
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """


def tarvese(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: mixed TreeNode if found else None
    """
    #find same node of p
    found = tarvese(root.left, p, q)
    if found:
        return found
    found = tarvese(root.right, p, q)
    if found:
        return found
    if isSameNode(root, p):
        ancestor = root
    if isSameNode(root.left, p):
        ancestor = root.left
    if isSameNode(ancestor.left, q) or isSameNode(ancestor.right, q):
        return root
    #not found break
    #found find same node of q
    #not found break


def isSameNode(a, b):
    """
    :type a: TreeNode
    :type b: TreeNode
    :rtype: bool
    """
    if not a and b:
        return False
    elif a and not b:
        return False
    elif not a and not b:
        return True
    if a.val == b.val:
        if isSameNode(a.left, b.left) and isSameNode(a.right, b.right):
            return True

    return False


class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        valid is same node by p == q
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == q:
            return p
        if p and not q:
            return p
        if q and not p:
            return q
        ancestor = self.tarvese(root, p, q)
        return ancestor if ancestor else root

    def tarvese(self, node, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: mixed TreeNode if found else None
        """
        if not node:
            return False
        if node.left:
            found = self.tarvese(node.left, p, q)
            if found:
                return found
        if node.right:
            found = self.tarvese(node.right, p, q)
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


class Solution4(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        valid is same node by p == q
        assuming the ancestor always exists
        using BST characters
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root is p or root is q:
            return root
        # handle exception
        if p.val != root.val != q.val:
            # p and q is not at the same side of root
            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                return root

            if p.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)

        if root.right:
            found = self.lowestCommonAncestor(root.right, p, q)
            if found:
                return found

        if containsNode(root, p) and containsNode(root, q):
            return root

        return False


def containsNode(a, b):
    if a is b:
        return True
    if a.left and containsNode(a.left, b):
        return True
    if a.right and containsNode(a.right, b):
        return True
    return False




#eof
