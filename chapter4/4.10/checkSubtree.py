

#We actually need to create 'None' nodes so they are printed and we can differentiate trees with same values (see hints)

#Time: O(n + m )
#Space: O(n + m )
#n number of nodes in tree1 , m number of nodes in tree2
def PreorderTrav(anode,string):
    if anode.value is None:
        string += 'N'
    string += str(anode.value)
    PreorderTrav(anode.leftchild)
    PreorderTrav(anode.rightchild)


def checkSubtree(tree1,tree2):
    firstString = "" #String builder
    PreorderTrav(tree1.root,firstString)
    secondString = "" #String builder
    PreorderTrav(tree2.root,secondString)
    if firstString.find(secondString) != -1:
        return True
    else:
        return False
