
#Time complexity O(n)
def interpolation_Search(array,value):
    
    lowerBound = 0
    mid = -1
    upperBound = 0
    while True:
        if  lowerBound == upperBound or array[lowerBound] == array[upperBound]:
            return False

        mid = lowerBound + ((upperBound - lowerBound)/(array[upperBound] -array[upperBound]- array[lowerBound])) * (value - array[lowerBound])
	


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



