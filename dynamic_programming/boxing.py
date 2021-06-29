 # 상자넣기 1965번
import sys

n = int(input())
box = list(map(int,sys.stdin.readline().rstrip().split()))

dp =[0]*n
dp[0]=1
for i in range(1,n):
    for j in range(i):
        if box[i]>box[j]:
            dp[i] = max(dp[i],dp[j])
    dp[i] +=1

print(max(dp))