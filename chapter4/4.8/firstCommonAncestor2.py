
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

    path1 = []
    path2 = []

    anode = p
    while anode is not None:
        path1.append(anode)
        anode = p.parent
    bnode = q
    while bnode is not None:
        path2.append(bnode)
        bnode = b.parent
    
    longest = path1 if len(path1) > len(path2) else path2
    smallest = path2 if len(path2) < len(path1) else path1

    diff = len(longest) - len(smallest)

    i = diff
    j = 0

    while longest[i] is not smallest[j]:
        i +=1
        j +=1
    if longest[i] is smallest[j]:
        return longest[i]
    else:
        return False
     
    
def in_subtree(x, p):
    if x is None:
        return False
    if x == p:
        return True
    return in_subtree(x.leftChild, p) or in_subtree(x.rightChild, p)

