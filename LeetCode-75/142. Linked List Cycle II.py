class Solution(object):
    def detectCycle(self, head):
        nodes = []
        node = head
        while node:
            if node in nodes: return node
            nodes.append(node)
            node = node.next
        return None