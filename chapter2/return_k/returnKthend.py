import LinkedList

linked_list = LinkedList.LinkedList([1,2,5,3,5,1,9,8,4,6,2,10,299,355,2])

def find_kth_end(head,k):
    if head is None:
        return 0

    index = find_kth_end(head.next,k) + 1

    if index == k:
        print(head.value)

    return index

find_kth_end(linked_list.head,8)


