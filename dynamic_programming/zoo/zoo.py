 #  동물원, 1309번
n = int(input());
dp = [[0,0,0] for _ in range(n)]

dp[0][0],dp[0][1],dp[0][2] = 1,1,1 # 사자가 없는 경우, 왼쪽 우리에 사자가 있는 경우, 오른쪽 우리에 사자가 있는 경우

for i in range(1,n):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%9901 # 현재 오른쪽,왼쪽 우리 둘 다 사자가 없는 경우
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901 # 왼쪽 우리에 사자가 있는 경우
    dp[i][2] = (dp[i-1][0] + dp[i-1][1])%9901 # 오른쪽 우리에 사자가 있는 경우

print(sum(dp[-1])%9901)