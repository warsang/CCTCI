
def sorted_search_no_size_brute(array,x):
    i = 0
    while True:
        try:
            if array[i] == x:
                return i
        except:
            return -1
        i += 1

def sorted_search_better(array,x):
    return find_length(array,x)

def find_length(array,x):
    increment = 1
    out_of_bounds = 0
    while out_of_bounds != -1:
        try:
            if array[increment] >= x:
                break
            increment *=2
        except:
            out_of_bounds = -1
    return binarySearch(array,x,increment//2,increment)

def binarySearch(array, x, low_bound, high_bound):
    
    while low_bound <= high_bound:
        mid = (low_bound + high_bound)//2
        try:
            middle = array[mid]
        except:
            middle = -1
        if middle > x or middle == -1:
            high_bound = mid -1
        elif middle < x:
            low_bound = mid +1
        else:
            return mid
    return -1


test_array = [1,4,6,24,95,3905,29043,10304094]
print(sorted_search_no_size_brute(test_array,6))
print(sorted_search_better(test_array,6))

