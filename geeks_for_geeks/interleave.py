
#Given three strings A, B and C your task is to complete the function isInterleave which returns true if C is an interleaving of A and B else returns false. C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters in individual strings is preserved.
#
#Input:
#The first line of input contains an input T denoting the no of test cases. Then T test cases follow. Each test case contains three space separated strings A, B, C.
#
#Output:
#For each test case output will be 1 if C is interleaving of string A and B else 0.


def isInterleaved(A,B,C,Aindex,Bindex,Cindex):
    #Step 1 compare char 1 of A and char1 of C
        #if match compare next character
    if Cindex == len(C):
        return True
    if A[Aindex] == C[Cindex]:
        Aindex +=1 
        Cindex +=1
        isInterleaved(A,B,C,Aindex,Bindex,Cindex)
    elif B[Bindex] == C[Cindex]:
        Cindex +=1
        Bindex +=1
        isInterleaved(A,B,C,Aindex,Bindex,Cindex)
    else:
        return False

print(isInterleaved('XYZA','BDC',"XYZABDC",0,0,0))
