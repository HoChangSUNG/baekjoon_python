import sys  # 메모리 초과
n,k = map(int,sys.stdin.readline().rstrip().split())
dp = [[0]*(k+1) for _ in range(n+1)]
num = [0]
for _ in range(n):
    num.append(int(sys.stdin.readline()))
for j in range(n+1):
    dp[j][0] = 1

for i in range(1,n+1):
    for j in range(1,k+1):
        if j>=num[i] :
            dp[i][j] = dp[i-1][j] + dp[i][j-num[i]]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])