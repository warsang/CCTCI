
#Bruteforce solution with slight optimisation
def findMagicBrute(array):

    for j in range(0,len(array)):
        if j == array[j]:
            return j
        if array[j] > j:
            return -1
    return -1

#Solution leveraging binary search
def findMagicFastCall(array):
    return findMagicFast(array,0,len(array)-1)

def findMagicFast(array,start,end):
    if end < start:
        return -1
    mid = (start + end)//2
    if(array[mid] == mid):
        return mid
    elif(array[mid] > mid):
        return findMagicFast(array,start,mid -1)
    else:
        return findMagicFast(array,mid + 1,end)

#Follow up

def findMagicFollowCall(array):
    return findMagicFollow(array,0,len(array)-1)

def findMagicFollow(array,start,end):
    if end < start or start < 0 or end >= len(array):
        return -1
    mid = (start + end)//2
    if array[mid]== mid :
        return mid
    left_end = min(mid-1 ,array[mid])
    left = findMagicFollow(array,start,left_end)
    if left != -1:
        return left
    right_start = max(mid +1, array[mid])
    return findMagicFollow(array,right_start,end)


def main():

    array = [1,2,2,5,7,10]
    result = findMagicBrute(array)
    if result == -1:
        print("No magic")
    else:
        print("The magic is " + str(result))

if __name__ == "__main__":
    main()
