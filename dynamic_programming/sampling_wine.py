 #  포도주 시식, 2156번
n = int(input())
amount = [0]
for _ in range(n):
    amount.append(int(input()))
dp=[0for _ in range(n+1)]
dp[1]=amount[1]
if(n>1):
    dp[2] =amount[1]+amount[2]
for i in range(3,n+1):
    dp[i] = max(amount[i]+amount[i-1]+dp[i-3],dp[i-2]+amount[i],dp[i-1])
print(dp[n])