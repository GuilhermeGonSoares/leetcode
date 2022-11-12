

class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    res = []
    if not root: return res
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        if curr:
            res.append(curr.val)
            stack.append(curr.left)
            stack.append(curr.right)
    return res[::-1]

#PRE-ORDEM:  ROOT -> LEFT -> RIGHT
#PÓS-ORDEM: LEFT -> RIGHT -> ROOT 
# ----- INVERTENDO PÓS-ORDEM -----
#ROOT -> RIGHT -> LEFT




''' Construct the following tree
               1
             /   \
            /     \
           2       3
          /  \      \
         /    \      \
        4      5      7
               /        \
              /          \
             6            8
                 
    '''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)
print(postorderTraversal(root))