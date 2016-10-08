"""
important knowledge:
height is different from balanceFactor
height is the depth of a node
balanceFactor is the height of left node minus the height of right node
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None.
class Solution(object):
    def isBalanced(self, root):
        """
        bad 92ms 58%
        a clean version
        too much recusive
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not self.isBalanced(root.left):
            return False

        if not self.isBalanced(root.right):
            return False

        if -2 < height(root.left) - height(root.right) < 2:
            return True
        else:
            return False
        return self.isBalanced(root)


def height(node):
    if not node:
        return 0
    elif node.left and not node.right:
        return height(node.left) + 1
    elif node.right and not node.left:
        return height(node.right) + 1
    elif node.left and node.right:
        return max(height(node.left), height(node.right)) + 1
    elif not node.left and not node.right:
        return 1


# [1,2,2,3,3,3,3,4,4,null,5,null,5]
# [1,null,2,null,3]
# [1,2,2,3,3,null,4,4,4,null,5,6,7,8,9,null]


class Solution1(object):
    def isBalanced(self, root):
        """
        nice 76 ms 90%
        get height and check balance factor at the same time
        :type root: TreeNode
        :rtype: bool
        """
        h = heightAndBalanced(root)
        return False if h is False else True


def heightAndBalanced(node):
    if not node:
        return 0
    h_l = heightAndBalanced(node.left)
    if h_l is False:
        return False
    h_r = heightAndBalanced(node.right)
    if h_r is False:
        return False

    return max(h_r, h_l) + 1 if -2 < h_l - h_r < 2 else False


class Solution2(object):
    def isBalanced(self, root):
        """
        bad 88ms 65%
        get height and check balance factor at the same time
        except this time right first
        :type root: TreeNode
        :rtype: bool
        """
        h = heightAndBalancedRightFirst(root)
        return False if h is False else True


def heightAndBalancedRightFirst(node):
    if not node:
        return 0
    h_r = heightAndBalanced(node.right)
    if h_r is False:
        return False
    h_l = heightAndBalanced(node.left)
    if h_l is False:
        return False

    return max(h_r, h_l) + 1 if -2 < h_l - h_r < 2 else False



#eof
