dp = [0 for i in range(11)]  # 1,2,3 더하기
dp[1],dp[2],dp[3]=1,2,4
for i in range(4,11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
test = int(input())
for i in range(test):
    n = int(input())
    print(dp[n])