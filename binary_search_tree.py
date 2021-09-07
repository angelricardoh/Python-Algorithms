class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def searchTree(node, value):
    if node == None:
        return None

    if node.value == value:
        return node

    if (value < node.value):
        return searchTree(node.left, value)
    else:
        return searchTree(node.right, value)

node_3 = Node(3, None, None)
node_5 = Node(5, None, None)
node_6 = Node(6, node_5, None)
node_4 = Node(4, node_3, node_6)
node_8 = Node(8, None, None)
node_7 = Node(7, node_4, node_8)
node_1 = Node(1, None, None)
node_2 = Node(2, node_1, node_7)

print(searchTree(node_2, 9))

    