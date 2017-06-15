import LinkedList #Could not be bothered implementing LL in python as I just did it in C

linked_listo = LinkedList.LinkedList([1,4,3,2,5,4,0,9,2,4,5,9,9,1])

def remove_duplicates(linked_list):

    value_counter = dict() 
    current = linked_list.head
    
    value_counter[current.value] = 1
    while current.next is not None: #while current.next
        if value_counter.get(current.next.value,0) == 1:
            #Remove element
            current.next = current.next.next
        else:
            value_counter[current.next.value] = 1
            current = current.next

def remove_duplicates_followup(linked_list):
    
    current = linked_list.head
    while current:
        runner=current
        while runner.next is not None:
            if current.value == runner.next.value:
                runner.next = runner.next.next
            else:
                runner=runner.next
        current=current.next

linked_listo = LinkedList.LinkedList([1,4,3,2,5,4,0,9,2,4,5,9,9,1])
print(linked_listo)
remove_duplicates(linked_listo)
print(linked_listo)
linked_listo = LinkedList.LinkedList([1,4,3,2,5,4,0,9,2,4,5,9,9,1])
remove_duplicates_followup(linked_listo)
print(linked_listo)



