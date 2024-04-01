import BTrees
import Same_Tree

def isSubtree(s, t):
    if not t:
        return True
    if not s:
        return False

    if Same_Tree(s, t):
        return True
    return isSubtree(s.left, t) or isSubtree(s.right, t)