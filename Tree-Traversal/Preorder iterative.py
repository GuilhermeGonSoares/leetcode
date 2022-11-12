

class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    res, stack = [], []
    if not root: return res
    current = root
    while current or stack:
        while current:
            res.append(current.val)
            stack.append(current)
            current = current.left
        current = stack.pop()
        current = current.right
    return res

'''
def preorderTraversal(root):
    res = []
    if not root: return res
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res
'''


''' Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    '''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
print(preorderTraversal(root))