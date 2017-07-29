#Method 1:


hashtable = {'a':0,'b':1,'c':2}

def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        leftarray = array[:mid]
        rightarray = array[mid:]

        mergeSort(rightarray)
        mergeSort(leftarray)

        i = 0
        j = 0
        k = 0
        while i < len(leftarray) and j < len(rightarray):
            if hashtable[leftarray[i]] < hashtable[rightarray[j]]:
            ### See my mergeSort implementation for the rest
                pass

def checkNonRepeat(string):
    results = []
    mergeSort(string)
    for i in range(len(string)-2):
        if string[i] != string[i+1] and string[i+1] != string[i+2]:
            results.append(string[i+1])
    return results
