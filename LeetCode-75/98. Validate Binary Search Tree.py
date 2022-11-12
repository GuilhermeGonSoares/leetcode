
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [(root, -float('inf'), float('inf'))]
        while len(stack) > 0:
            r, lower, upper = stack.pop()
            if not r:
                continue
            val = r.val
            if val <= lower or val >= upper:
                return False
            stack.append((r.right, val, upper))
            stack.append((r.left, lower, val))
        return True
