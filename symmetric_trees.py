class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if root is None:
        return True
    return sym(root.left, root.right)

def sym(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif (root1 is None) != (root2 is None) or root1.val != root2.val:
        return False
    else:
        return sym(root1.left, root2.right) and sym(root1.right, root2.left)

root_symmetric = TreeNode(1)
root_symmetric.left = TreeNode(2, TreeNode(3), TreeNode(4))
root_symmetric.right = TreeNode(2, TreeNode(4), TreeNode(3))

# Constructing a non-symmetric tree
root_non_symmetric = TreeNode(1)
root_non_symmetric.left = TreeNode(2, None, TreeNode(3))
root_non_symmetric.right = TreeNode(2, None, TreeNode(3))

print(is_symmetric(root_symmetric)) 
print(is_symmetric(root_non_symmetric))  
