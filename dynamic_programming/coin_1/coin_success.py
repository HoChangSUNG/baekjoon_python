 #  동전1, 2293번
n, k = map(int,input().split())

dp = [0]*(k+1) # 열의 개수(0~k)
dp[0] = 1
for _ in range(n):
    coin = int(input())
    for j in range(1,k+1):
        if j>=coin:
            dp[j]+=dp[j-coin]


print(dp[k])