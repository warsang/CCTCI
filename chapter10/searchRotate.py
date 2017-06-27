
def searchAndRotate(array,searched,index):
    mid = (len(array)//2) - 1
    if array[mid] == searched:
        return mid,index + mid
    if array[0] < array[mid]:
        #Left is normally ordered
        if searched >= array[0] and searched < array[mid] : 
            return  searchAndRotate(array[:mid],searched,mid)
        else:
            return searchAndRotate(array[mid+1:],searched,index + mid + 1)
    elif array[0] > array[mid]:
        #Right normally ordered
        if searched <= array[-1] and searched > array[mid]:
            return searchAndRotate(array[mid+1:],searched,index + mid + 1)
        else:
            return searchAndRotate(array[:mid],searched,mid)
    elif array[0] == array[mid]:
        if array[mid] != array[-1]:
            return searchAndRotate(array[mid+1:],searched,index + mid + 1)
        else:
            result = searchAndRotate(array[:mid],searched,mid)
            if result == False:
                return searchAndRotate(array[mid+1:],searched,index + mid + 1)
            else:
                return result
    return False

test = [15,16,19,20,25,1,3,4,5,7,10,14]
index = 0
print(searchAndRotate(test,4,index))
