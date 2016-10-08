# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def travel(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                travel(node.left, level+1)
            if node.right:
                travel(node.right, level+1)
        if root:
            travel(root, 0)
        return res


class Solution1(object):
    def levelOrder(self, root):
        """
        using target list as arguments instead of level
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root:
            lt = []
            res.append(lt)
            travel(root, 0)
        return res


def travel(node, lt):
    lt.append(node.val)
    if node.left:
        travel(node.left, lt)
    if node.right:
        travel(node.right, lt)


"""
https://leetcode.com/discuss/62528/5-6-lines-fast-python-solution-48-ms

level is a list of the nodes in the current level.
Keep appending a list of the values of these nodes to ans and then
    updating level with all the nodes in the next level (kids) until
    it reaches an empty level.
Python's list comprehension makes it easier to deal with
    many conditions in a concise manner.
"""

# Solution 1, (6 lines)


def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        LRpair = [(node.left, node.right) for node in level]
        level = [leaf for LR in LRpair for leaf in LR if leaf]
    return ans

# Solution 2, (5 lines), same idea but
# use only one list comprehension in while loop to get the next level


def levelOrder1(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        level = [kid for n in level for kid in (n.left, n.right) if kid]
    return ans

# Solution 3 (10 lines),
# just an expansion of solution 1&2 for better understanding.


def levelOrder2(self, root):
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans



print not not [None]
print not not [0]
print not not []
print not not 0


testCases = [
    """
        [1,2,2,3,3,3,3,4,null,4,4,null,4,4,4,5,5,null,null],
        [],
    """
]
#eof
