class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = Node(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = Node(value)
        else:
            self.value = value

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.value)
        print_inorder(root.right)

def print_preorder(root):
    if root:
        print(root.value)
        print_preorder(root.left)
        print_preorder(root.right)

def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.value)

# Function to  print level order traversal of tree
def print_levelorder(root):
    h = height(root)
    for i in range(1, h+1):
        print_current_level(root, i)
 
 
# Print nodes at a current level
def print_current_level(root , level):
    if root is None:
        return
    if level == 1:
        print(root.value, end=" ")
    elif level > 1 :
        print_current_level(root.left , level-1)
        print_current_level(root.right , level-1)
 
 
""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
def height(node):
    if node is None:
        return 0
    else :
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# print("Preorder traversal of binary tree is")
# print_preorder(root)
 
# print("\nInorder traversal of binary tree is")
# print_inorder(root)
 
# print("\nPostorder traversal of binary tree is")
# print_postorder(root)

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal of binary tree is")
print_preorder(root)
 
print("\nInorder traversal of binary tree is")
print_inorder(root)
 
print("\nPostorder traversal of binary tree is")
print_postorder(root)

print("\nLevelorder traversal of binary tree is")
print_levelorder(root)