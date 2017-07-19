
#Given three strings A, B and C your task is to complete the function isInterleave which returns true if C is an interleaving of A and B else returns false. C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters in individual strings is preserved.
#
#Input:
#The first line of input contains an input T denoting the no of test cases. Then T test cases follow. Each test case contains three space separated strings A, B, C.
#
#Output:
#For each test case output will be 1 if C is interleaving of string A and B else 0.


#Time Complexity: For a string C of length N
#O(1^N) if A == B O(2^N)
#Memory Complexity:

def isInterleave(A,B,C,Aindex,Bindex,Cindex):
    #Step 1 compare char 1 of A and char1 of C
        #if match compare next character
    if len(A) == 0:
        return B == C
    elif len(B) == 0:
        return A == C
    if A[0] == C[0] and B[0] == C[0]:
        return max(isInterleave(A[1:],B,C[1:]),isInterleave(A,B[1:],C[1:]))
    elif A[0] == C[0]:
        return isInterleave(A[1:],B,C[1:])
    elif B[0] == C[0]:
        return isInterleave(A,B[1:],C[1:])
    else:
        return False

print(isInterleave('XYZA','XDC',"XYZAXDC",0,0,0))
