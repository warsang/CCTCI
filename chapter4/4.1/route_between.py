class Graph(object):
        
    def __init__(self,nodes):
        self.nodes = nodes # List of Nodes

    def search(self,node):
        if node is None:
            raise "Value Error"
        if self.visit(node) == True:
            return True
        node.visited = True
        for each_node in node.children:
            if each_node.visited == False:
                self.search(each_node)
        else:
            return False

    def visit(self,node):
        if node.name == 9:
            return True
    
class Node(object):
    
    def __init__(self,name,children):
        self.name = name
        self.children = children # List of Nodes
        self.visited = False

graph_links = {
        1:[5,2],
        2:[8],
        3:[9],
        8:[3],
        6:[5],
        9:[6]
        }

def main():
    node_list = []
    fake_node = Node(23,[])
    graph = Graph(node_list)
    for key in graph_links:
        graph.nodes.append(Node(key,[]))
    #Not great init in complexity time but that is not what we are looking at. Plus can be improved!
    for key,value in graph_links.items():
        for node in graph.nodes:
            if key == node.name:
                for element in value:
                    for node_2 in graph.nodes:
                        if node_2.name == element:
                            node.children.append(node_2)
    print(graph.search(graph.nodes[5]))
    print(graph.search(fake_node))

if __name__=="__main__":
    main()
