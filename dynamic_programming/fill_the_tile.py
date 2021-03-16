 #  타일 채우기
n = int(input())
dp = [0 for _ in range(31)]
dp[0] =1
dp[2] =3
if n%2==0:
    for i in range(4,n+1,2):
        dp[i] = 3*dp[i-2] + 2*(sum(dp[:i-2]))
    print(dp[n])
else:
    print(dp[n])
