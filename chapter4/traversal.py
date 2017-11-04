def preOrderTraversal(node):
    if node is not None:
       #Do something with node
        if node.value == 5:
            print(node.value)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)
 

def postOrderTraversal(node):
    if node is not None:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        #do something with node
        if node.value == 5:
            print(node.value)
 

def inOrderTraversal(node):
    if node is not None:
        inOrderTraversal(node.left)
        #Do something with node
        if node.value == 5:
            print(node.value)
        inOrderTraversal(node.right)
        
