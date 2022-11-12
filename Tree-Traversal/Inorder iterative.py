'''
.Crie uma pilha vazia e envie o nó raiz.
.Declarar uma variável para rastrear o nó atual
.Execute o loop while até que a pilha não esteja vazia ou o nó atual seja Nenhum
.Continuamos adicionando o nó atual à esquerda na pilha.
.Quando o nó atual se torna nenhum e a pilha não está vazia, retiramos o elemento da pilha e o atribuímos como o nó atual.
.processar o nó atual e, em seguida, definir o nó atual à direita do nó atual.
'''

class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    res = []
    if not root: return res
    stack = []
    curr_node = root
    while curr_node or stack:
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        curr_node = stack.pop()
        res.append(curr_node.val)
        curr_node = curr_node.right
    return res



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

print(inorderTraversal(root))