#Time complexity: O(A+B) with A and B length of two llists
#Memory complexity: O(1)


class node(object):

    def __init__(self,value,nxt = None):
        self.value = value
        self.nxt = nxt

class linked_list(object):

    def __init__(self,head = None, tail = None):
        self.head = head
        self.tail = tail

    def __len__(self):
        res = 0
        node = self.head
        while True:
            if node.nxt is not None:
                res += 1
                node = node.nxt
            else:
                return res

def intersection(llist1,llist2):

    #Different tails => not llist
    if llist1.tail is not llist2.tail:
        return False
    
    shorter = llist1 if len(llist1) < len(llist2) else llist2
    longer = llist2 if len(llist2) > len(llist1) else llist1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for i in range(diff):
        longer_node = longer_node.nxt

    while shorter_node is not longer_node:
        shorter_node = shorter_node.nxt
        longer_node = longer_node.nxt
    
    return longer_node
