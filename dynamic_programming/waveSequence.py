# 파도반 수열, 9461번
import sys
def sequence(n):
    dp = [0]*100
    dp[0],dp[1],dp[2]=1,1,1
    for i in range(3,n):
        dp[i] = dp[i-3]+dp[i-2]
    return dp[n-1]
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(sequence(n))