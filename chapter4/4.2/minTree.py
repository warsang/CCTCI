array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]

class Node(object):

    def __init__(self,item):
        self.left = None
        self.right = None
        self.val= item

    def __str__(self):
        return '( Left : '+str(self.left) + " Middle : " + str(self.val) + " Right : " + str(self.right)+')\n' #Not my string, couldn't figure out how to represent properly!

def place_in_tree(array,start,end):
    if start > end:
        return
    mid = (start + end)//2
    root_node = Node(array[mid])
    root_node.left = place_in_tree(array,start,mid-1)
    root_node.right = place_in_tree(array,mid+1,end)
    return root_node

print(place_in_tree(array, 0, len(array) - 1))
