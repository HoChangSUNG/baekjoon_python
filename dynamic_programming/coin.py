 #  동전,9084번
import sys

def solution(n,m,coins):
    dp = [0 for _ in range(m+1)]
    dp[0] =1

    for coin in coins:
        for j in range(1,m+1):
            if(j>=coin):
                dp[j] += dp[j-coin]
    print(dp[-1])


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    coins = list(map(int,sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    solution(n,m,coins)