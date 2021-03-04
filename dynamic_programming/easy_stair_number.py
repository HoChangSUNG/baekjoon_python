 #  쉬운 계단 수
dp = [[0 for _ in range(10)]for _ in range(100)]
n = int(input())
dp[0][1],dp[0][2],dp[0][3],dp[0][4],dp[0][5],dp[0][6],dp[0][7],dp[0][8],dp[0][9] = 1,1,1,1,1,1,1,1,1
for i in range(1,n):
    # dp[i][0] = dp[i-1][1]
    # dp[i][1] = dp[i-1][0]+dp[i-1][2]
    # dp[i][2] = dp[i-1][1]+dp[i-1][3]
    # dp[i][3] = dp[i-1][2]+dp[i-1][4]
    # dp[i][4] = dp[i-1][3]+dp[i-1][5]
    # dp[i][5] = dp[i-1][4]+dp[i-1][6]
    # dp[i][6] = dp[i-1][5]+dp[i-1][7]
    # dp[i][7] = dp[i-1][6]+dp[i-1][8]
    # dp[i][8] = dp[i-1][7]+dp[i-1][9]
    # dp[i][9] = dp[i-1][8]
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j+1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n-1])%1000000000)