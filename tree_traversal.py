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

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val)
        print_inorder(root.right)

def print_preorder(root):
    if root:
        print(root.val)
        print_preorder(root.left)
        print_preorder(root.right)

def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val)

# Function to  print level order traversal of tree
def print_levelorder(root):
    h = height(root)
    for i in range(1, h+1):
        print_current_level(root, i)
 
 
# Print TreeNodes at a current level
def print_current_level(root , level):
    if root is None:
        return
    if level == 1:
        print(root.val, end=" ")
    elif level > 1 :
        print_current_level(root.left , level-1)
        print_current_level(root.right , level-1)
 
 
""" Compute the height of a tree--the number of TreeNodes
    along the longest path from the root TreeNode down to
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

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# print("Preorder traversal of binary tree is")
# print_preorder(root)
 
# print("\nInorder traversal of binary tree is")
# print_inorder(root)
 
# print("\nPostorder traversal of binary tree is")
# print_postorder(root)

# Driver program to test above function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder traversal of binary tree is")
print_preorder(root)
 
print("\nInorder traversal of binary tree is")
print_inorder(root)
 
print("\nPostorder traversal of binary tree is")
print_postorder(root)

print("\nLevelorder traversal of binary tree is")
print_levelorder(root)