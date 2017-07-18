
#Time complexity:
#Recursive function with two calls. O(2^N) on average, though usually less as not each level is completly full
#height of the BST
#Memory complexity:
#Each recursive call is delt upon a part of the tree so O(N)

class node(object):

    def __init__(self,value,childOne = None,childTwo = None,parent = None):

        self.value = value
        self.childOne = childOne
        self.childTwo = childTwo
        self.parent = parent


def main():
    
    four = node(4)
    eight = node(8)
    twelve = node(12)
    ten = node(10)
    fourteen = node(14)
    twenty = node(20)
    twentytwo = node(22)

    #Build tree:

    four.parent = eight
    eight.parent = twenty
    ten.parent = twelve
    twelve.parent = eight
    fourteen.parent = twelve
    twentytwo.parent = twenty
    
    eight.childOne = four
    eight.childTwo = twelve
    twelve.childOne = ten
    twelve.childTwo = fourteen
    twenty.childOne = eight
    twenty.childTwo = twentytwo
    
    print(checkBSTcaller(twenty))
    
    #Change BST

    thirtyfive = node(35)
    thirtyfive.parent = four
    four.childOne = thirtyfive

    print(checkBSTcaller(twenty))

def checkBSTcaller(treeNode):
    return checkBST(treeNode,None,None)

def checkBST(treeNode,minimum,maximum):

    if treeNode is None:
        return True
    if((minimum is not None and treeNode.value <= minimum) or (maximum is not None and treeNode.value > maximum)):
        return False
    if((checkBST(treeNode.childOne,minimum,treeNode.value) == False) or (checkBST(treeNode.childTwo,treeNode.value,maximum))== False):
        return False
    return True

if __name__ == "__main__":
    main()
