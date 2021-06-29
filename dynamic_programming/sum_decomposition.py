 #  합분해, 2225번
import sys
n,k = map(int,sys.stdin.readline().split())
dp = [[0 for _ in range(n+1)]for _ in range(k+1)]
for i in range(1,k+1):
    dp[i][1] = i
for j in range(1,n+1):
    dp[1][j] = 1
for j in range(2,n+1):
    for i in range(2,k+1):
        for k in range(1,i+1):
            dp[i][j]+=dp[k][j-1]

print(dp[k][n]%1000000000)