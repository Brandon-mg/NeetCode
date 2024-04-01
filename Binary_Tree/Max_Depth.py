import BTrees

def maxDepth(root):
        if not root:
            return 0

        return 1 + max(maxDepth(root.left), maxDepth(root.right))

if __name__ == "__main__":
    preorder = [4,2,7,1,3,6,9]
    inorder = [1,2,3,4,6,7,8]
    root = BTrees.buildTree(preorder, inorder)
    print(maxDepth(root))