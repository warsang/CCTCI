

class node(object):

    def __init__(self,name,child):
        self.name = name
        self.child = child

def main():
    
    llist = []
    f = node("f",None)
    e = node("e",f)
    d = node("d",e)
    c = node("c",d)
    b = node("b",c)
    a = node("a",b)
    
    llist = [a,b,c,d,e,f]

    deleteNode(c)

    Node = a
    while True:
        if Node.child is None:
            print(Node.name)
            break
        else:
            print( Node.name + "->")
            Node = Node.child

def deleteNode(node):
    
    if node.child is None:
        return
    replaceNodeByChild(node)

def replaceNodeByChild(node):
    node.name = node.child.name
    node.child = node.child.child

if __name__ == "__main__":
    main()
