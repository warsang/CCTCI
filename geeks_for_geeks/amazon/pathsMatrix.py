def numberOfPaths(m,n):

    if m == 1 or n == 1:
        return 1

    return numberOfPaths(m-1,n) + numberOfPaths(m,n-1)


def numberOfPathsRec(m,n):

    count = [[0 for x in range(m)] for y in range(n)]

    for i in range(m):
        count[i][0] = 1
    
    for j in range(n):
        count[0][j] = 1

    for i in range(1,m):
        for j in range(n):
            count[i][j] = count[i-1][j]

    return count[m-1][n-1]

print(numberOfPaths(3,3))
print(numberOfPathsRec(3,3))
