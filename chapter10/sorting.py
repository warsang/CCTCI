

#Time complexity: Always O(nlog(n))
#Memory: O(n)

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

#Time complexity: O(n^2)
#Memory: O(1)
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentValue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentValue:
            alist[position] = alist[position-1]
            position = position - 1

        alist[postion]  = currentValue


def heapify(arr,n,i):
    #Find largest amongst root and children
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    #If root is not the largest, swap with largest and continue heapifying
    if largest != i :
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest)

#Time: O(nlogn)
#Mem: O(1)

def heapSort(array):
    n = len(arr)

    #Build max heap
    for i in range(n,0,-1):
        heapify(arr,n,i)
    
    for i in range(n-1,0,-1):
        #swap
        arr[i],arr[0] = arr[0],arr[i]
        #heapify root element
        heapify(arr,i,0)

#Time: O(n^2)
#Mem: O(1)

def selectionSort(array):
    
    for i in range(len(array)-1):
        mini = i
        for j in range(i+1,len(array)):
            if array[j] < array[mini]:
                mini = j

        if mini != i:
            array[mini] ,array[i] = array[i],array[mini]

#Time: O(n^2)
#Mem: O(1)

def bubbleSort(array):
    #Processs should be repeated n-1 times for n elements
    for i in range(len(array) - 1):
        for j in range(len(array) -1):
            if array[j] < array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]


#Time: O(nlogn)
#Worst: O(N^2)
#mem: O(logn)
def quickSort(alist):
    _quickSort(alist,0,len(alist) - 1)

def _quickSort(alist,first,last):
    if first < last:
        splitPoint = partition(alist,first,last)
        
        _quickSort(alist,first,splitPoint -1)
        _quickSort(alist,splitPoint + 1,last)

def partition(alist, first,last):
    pivotValue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotValue:
            leftmark += 1

        while rightmark >= leftmark and alist[rightmark] >= pivotValue:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
    
    alist[first],alist[rightmark] = alist[rightmark],alist[first]
        



