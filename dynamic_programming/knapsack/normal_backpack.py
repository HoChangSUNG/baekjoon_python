  #  평범한 배낭 12865번
import sys
n,k = map(int, sys.stdin.readline().rstrip().split())

limit = k #  최대 무게
stuff = [[0.0]] # weight, value 순

for i in range(n):
    stuff.append(list(map(int,sys.stdin.readline().rstrip().split())))


dp = [[0]*(limit+1)for _ in range(len(stuff))]
for i in range(1,len(stuff)):
    for j in range(1,limit+1):
        weight = stuff[i][0]
        value = stuff[i][1]
        if j>=weight:
            dp[i][j] = max(dp[i-1][j-weight]+value,dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[len(stuff)-1][limit])