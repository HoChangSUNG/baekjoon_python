#LCS, 9251번
import sys
firstString = sys.stdin.readline().rstrip()
secondString = sys.stdin.readline().rstrip()
dp = [[0 for _ in range(len(firstString)+1)]for _ in range(len(secondString)+1)]

for i in range(1,len(dp)):
    for j in range(1,len(dp[0])):

        if firstString[j-1] == secondString[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1]) # ->lcs길이 출력

# lcs구하기
lcs=""
i,j=len(secondString),len(firstString)
while i>0 and j>0:
    if dp[i][j]==dp[i-1][j]:
        i=i-1
    elif dp[i][j]==dp[i][j-1]:
        j=j-1
    else:
        lcs= secondString[i-1] + lcs
        i,j=i-1,j-1
print(lcs) # -> lcs 출력