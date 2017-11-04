
def countTransform(a,b):
    n = len(a)
    m = len(b)

    if(m == 0):
        return 1

    dp = [[None] * (m+1)]*(n+1)

    for i in range(0,m):
        for j in range(i,n):
            if i == 0:
                if a[j] == b[i] and j == 0:
                    dp[i][j] = 1
                elif a[j] == b[i]:
                    dp[i][j] = dp[i][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
            else:
                if a[j] == b[i]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
    print(str(dp))
    return dp[m - 1][n - 1]

countTransform('abcccdf','abccdf')
