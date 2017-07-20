

def sorted_merge(A,B,helper):
    i = 0 # B's index
    j = 0 # A's index
    k = 0 # helper index
    while i < len(B):
        if helper[k] is not None and helper[k] <= B[i]:
            if j >= len(A):
                A.append(helper[k])
            else:
                A[j] = helper[k]
            k += 1
        else:
            if j >= len(A):
                A.append(B[i])
            else:
                A[j] = B[i]
            i +=1
        j +=1
    i = 0
    while helper[k+i] is not None:
        A.append(helper[k+i])
        i += 1

def sorted_merge_backwards(A,B,a_end):
    i = len(B) - 1 #Index of last element in B
    #j = len(A) - 1 
    j = a_end
    #Index of last element in A
    #If A is an array with enough space for B,to get it's last element
    #we would use a "while A[i] is not None:"
    k = i + j + 1 #Merged array

    while i >= 0 and j >= 0:
        if j >= 0 and A[j] > B[i]:
            A[k] = A[j]
            j -= 1
        else:
            A[k] = B[i]
            i -=1
        k -=1

    while i>=0:
        A[k] = B[i]
        i -=1
        k -=1


A = [1,2,4,56,68,79,159,200]
B = [20,30,40,60,80]
helper = [None]*(len(A)+1)
for i in range(len(A)):
    helper[i] = A[i]
sorted_merge(A,B,helper)
print(A)
A = [1,2,4,56,68,79,159,200,None,None,None,None,None]
B = [20,30,40,60,80]
sorted_merge_backwards(A,B,7)
print(A)
