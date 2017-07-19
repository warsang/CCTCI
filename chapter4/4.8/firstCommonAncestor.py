
class node(object):

    def __init__(self,value,parent = None,leftChild=None,rightChild=None):
        self.value = value
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild

def firstCommonAncestor(root,p,q):
    if not in_subtree(root,p) or not in_subtree(root,q):
        return None
    return _firstCommonAncestor(root,p,q)

def _firstCommonAncestor(root,p,q):
    if root is None:
        return None
    if root == p or root == q:
        return root
    is_p_on_the_left = in_subtree(root.leftChild, p) # takes 1/2 the number of calls each time
    is_q_on_the_left = in_subtree(root.leftChild, q)
    if is_p_on_the_left != is_q_on_the_left:
        return root
    if is_p_on_the_left:
        return _firstCommonAncestor(root.leftChild, p, q)
    else:
        return _firstCommonAncestor(root.rightChild, p, q)

def in_subtree(x, p):
    if x is None:
        return False
    if x == p:
        return True
    return in_subtree(x.leftChild, p) or in_subtree(x.rightChild, p)

