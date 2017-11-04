
INT_MAX=32767

def eggDrop(eggNum,floorNum):
    
    eggFloor = [[None for i in range(k+1)] for j in range(n+1)]
    
    #Base cases
    #1 try for one floor
    #0 try for 0 floor
    for i in range(1,n+1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
    
    #j trials for one egg
    for j in range(1,k+1):
        eggFloor[1][j] = j

    for i in range(2,n+1):
        for j in range(2,k+1):
            eggFloor[i][j] = INT_MAX
            for x in range(1,j+1):
                res = 1 + max(eggFloor[i-1][x-1],eggFloor[i][j-x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res

    return eggFloor[n][k]

