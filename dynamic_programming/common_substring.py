# 공통 부분 문자열, 5582번

import sys
str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()
dp= [[0 for _ in range(len(str1)+1)]for _ in range(len(str2)+1)]

result = 0
for i in range(1,len(str2)+1):
    for j in range(1,len(str1)+1):
        if str1[j-1]==str2[i-1]:
            dp[i][j] = dp[i-1][j-1]+1
            result = max(result,dp[i][j])
print(result)
