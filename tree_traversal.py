class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left:
                    self.left.insert(val)
                else:
                    self.left = TreeNode(val)
            else:
                if self.right:
                    self.right.insert(val)
                else:
                    self.right = TreeNode(val)
        else:
            self.val = val

def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.val)
        print_inorder(node.right)

def print_preorder(node):
    if node:
        print(node.val)
        print_preorder(node.left)
        print_preorder(node.right)

def print_postorder(node):
    if node:
        print_postorder(node.left)
        print_postorder(node.right)
        print(node.val)

# Function to  print level order traversal of tree
def print_levelorder(node):
    h = height(node)
    for i in range(1, h+1):
        print_current_level(node, i)
 
 
# Print TreeNodes at a current level
def print_current_level(node , level):
    if node is None:
        return
    if level == 1:
        print(node.val, end=" ")
    elif level > 1 :
        print_current_level(node.left , level-1)
        print_current_level(node.right , level-1)
 
 
""" Compute the height of a tree--the number of TreeNodes
    along the longest path from the node TreeNode down to
    the farthest leaf TreeNode
"""
def height(TreeNode):
    if TreeNode is None:
        return 0
    else :
        # Compute the height of each subtree
        lheight = height(TreeNode.left)
        rheight = height(TreeNode.right)
 
        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1

# node = TreeNode(1)
# node.left = TreeNode(2)
# node.right = TreeNode(3)
# node.left.left = TreeNode(4)
# node.left.right = TreeNode(5)
# print("Preorder traversal of binary tree is")
# print_preorder(node)
 
# print("\nInorder traversal of binary tree is")
# print_inorder(node)
 
# print("\nPostorder traversal of binary tree is")
# print_postorder(node)

# Driver program to test above function
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)

print("Preorder traversal of binary tree is")
print_preorder(node)
 
print("\nInorder traversal of binary tree is")
print_inorder(node)
 
print("\nPostorder traversal of binary tree is")
print_postorder(node)

print("\nLevelorder traversal of binary tree is")
print_levelorder(node)