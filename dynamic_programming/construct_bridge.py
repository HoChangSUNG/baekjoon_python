  #  다리놓기, 1010번
import sys

#   0 1 2 3 4 5        서\동 기준
# 0 1 1 1 1 1 1
# 1   1 2 3 4 5
# 2     1 3 6 10
# 3       1 4 10



def bridge(west,east):
    dp = [[0 for _ in range(east+1)] for _ in range(west+1)]
    for j in range(1,east+1):
        dp[0][j] = 1
    for i in range(1,west+1):
        for j in range(1,east+1):
            if(i == j):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    return dp[west][east]

n = int(input())
for _ in range(n):
    west,east = map(int,sys.stdin.readline().rstrip().split())
    print(bridge(west,east))
