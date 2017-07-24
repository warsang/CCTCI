#BFS as described in CTCI p 108
#Please note that node object needs adjacent attribute (list of adjacent nodes)



#Time Complexity: O(|V| +|E|) 
#V = number of nodes, E = number of edges 
def bfsearch(node,searched):
    root = node

    queue = []
    root.marked = True
    queue.append(root)
    
    while len(queue) != 0:
        #Remove first in
        anode = queue[0]
        if len(queue) != 1:
            queue = queue[1:]
        else:
            queue = []
        #Do something with anode
        if anode.value == searched.value:
            return anode
        for n in anode.adjacent:
            if n.marked == False:
                n.marked = True
                queue.append(n)

