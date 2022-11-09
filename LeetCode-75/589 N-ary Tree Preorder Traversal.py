
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        l = [root.val] if root else []
        nodes = root.children if root else []
        while nodes:
            node = nodes.pop(0)
            print(node.val)
            l.append(node.val)
            nodes = node.children + nodes
        return l

#[2,4]
#l = [3,5,6]








            