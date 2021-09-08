# 구간 합 구하기, 11660번
import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
dp = [[0]*(n+1)]
for _ in range(n):
    dp.append([0]+list(map(int,sys.stdin.readline().rstrip().split())))
for i in range(0,len(dp)):
    for j in range(1,len(dp[i])):
        dp[i][j] +=dp[i][j-1]

for _ in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().rstrip().split())
    result = 0
    for i in range(x1,x2+1):
        result += (dp[i][y2]-dp[i][y1-1])
        # print(i,y2,y1-1)
    print(result)