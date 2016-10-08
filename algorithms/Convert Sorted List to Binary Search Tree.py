# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return TreeNode('b')


class AVLTree(object):

    def insert(self):
        pass

    def balance(self):
        pass


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

rs = Solution().sortedListToBST(TreeNode('a')).val
print(rs)

#eof
