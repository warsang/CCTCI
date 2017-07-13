
#Time complexity:
#O(log N) is the time complexity of a search. Worst case is O(h) with h the 
#height of the BST
#Memory complexity:
#O(N) with N = number of elements in tree

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

    result = inOrderSuccess(fourteen)
    print(result.value)
    result = inOrderSuccess(eight)
    print(result.value)
    result = inOrderSuccess(ten)
    print(result.value)

def inOrderSuccess(anode):

    if anode.childTwo is not None:
        root = anode.childTwo
        while True:
            if root.childOne is not None:
                root = root.childOne
            else:
                return root
    else:
        while True:
            if anode.parent.value >= anode.value:
                return anode.parent
            else:
                anode = anode.parent
if __name__ == "__main__":
    main()
