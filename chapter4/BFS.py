#BFS as described in CTCI p 108
#Please note that node object needs adjacent attribute (list of adjacent nodes)



#Time Complexity: O(|V| +|E|) 
#V = number of nodes, E = number of edges 
def bfsearch(node):
    root = node

    queue = []
    root.marked = True
    queue.append(root)
    
    while len(queue) != 0:
        #Remove first in
        anode = queue[0]
        queue = queue[1:]
        #Do something with anode
        if anode == 5:
            print(anode.value)
        for n in anode.adjacent:
            if n.marked == False:
                n.marked = True
                queue.append(n)

