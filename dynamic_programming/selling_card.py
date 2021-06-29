 #  카드 구매하기, 11052번
import sys
n = int(input())
cards = list(map(int,sys.stdin.readline().rstrip().split()))
dp=[0]
for i in range(1,n+1):
    dp.append(cards[i-1])
    for j in range(1,i//2+1):
        dp[i] = max(dp[i],dp[j]+dp[i-j])
print(dp[n])