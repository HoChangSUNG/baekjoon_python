 #  동전2 2294번
n, k =map(int,input().split())

dp = [0]*(k+1)
for _ in range(n):
    coin = int(input())
    for j in range(1,k+1):
        if coin<=j:
            if coin == j: dp[j] = 1
            if dp[j-coin] !=0 :
                if dp[j] ==0 :
                    dp[j]=dp[j-coin]+1
                else :
                    dp[j] = min(dp[j],dp[j-coin]+1)
if dp[-1]==0:
    print(-1)
else:
    print(dp[-1])

