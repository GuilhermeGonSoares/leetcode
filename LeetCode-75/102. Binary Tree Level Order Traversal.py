# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        l = [[root.val]] if root else []
        node_childs = []
        if root: 
            node_childs.append(root.left)
            node_childs.append(root.right)
        while node_childs:
            temp = node_childs[::]
            l_temp = []
            while temp:
                node_childs.pop(0)
                node = temp.pop(0)
                if node:
                    l_temp.append(node.val)
                    if node.left: node_childs.append(node.left)
                    if node.right: node_childs.append(node.right)
            if l_temp != []: l.append(l_temp)
        return l