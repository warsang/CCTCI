
#Time complexity O(n)
def linear_search(alist,value):

    for i in range(0,len(alist)):
        if alist[i] == value:
            return i
    return None

#Time complexity O(log(n))
def binary_search(alist,value):

    lowerBound = 0
    upperBound = len(alist) - 1

    while True:
        if upperBound < lowerBound:
            return None

        mid = (upperBound - lowerBound)//2

        if alist[mid] > value:
            lowerBound = mid + 1

        elif alist[mid] < value:
            upperBound = mid - 1

        else: #if alist[mid] == value:
            return mid



