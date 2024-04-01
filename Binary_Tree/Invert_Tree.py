import BTrees

def invertTree(self, root):
    if root == None:
        return root
    right = self.invertTree(root.left)
    left = self.invertTree(root.right)
    root.left = left
    root.right = right
    return root

if __name__ == "__main__":
    preorder = [4,2,7,1,3,6,9]
    inorder = [1,2,3,4,6,7,8]
    root = BTrees.buildTree(preorder, inorder)
    root= invertTree(root)