#LCS 3, 1958번
import sys

def getLcs(firstString,secondString,thirdString):
    #lcs길이 구하기
    dp = [[[0 for _ in range(len(thirdString)+1)] for _ in range(len(secondString)+1)]for _ in range(len(firstString)+1)]
    for i in range(1,len(firstString)+1):
        for j in range(1,len(secondString)+1):
            for k in range(1,len(thirdString)+1):
                if firstString[i-1]==secondString[j-1] and secondString[j-1]==thirdString[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1]+1
                else:
                    dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1],dp[i-1][j-1][k],dp[i][j-1][k-1],dp[i-1][j][k-1])
    #lcs구하기
    i,j,k = len(firstString),len(secondString),len(thirdString)
    lcs = ""
    while i>0 and j>0 and k>0:
        if dp[i][j][k] == dp[i-1][j][k]:
            i=i-1
        elif dp[i][j][k] == dp[i][j-1][k] :
            j=j-1
        elif dp[i][j][k] == dp[i][j][k-1]:
            k=k-1
        elif dp[i][j][k] == dp[i-1][j-1][k]:
            i=i-1
            j=j-1
        elif dp[i][j][k] == dp[i][j-1][k-1]:
            j=j-1
            k=k-1
        elif dp[i][j][k] == dp[i-1][j][k-1]:
            i=i-1
            k=k-1
        else:
            lcs = firstString[i-1]+lcs
            i-=1
            j-=1
            k-=1
    # return lcs # -> lcs리턴
    return dp[-1][-1][-1] # -> lcs길이 리턴

firstString = sys.stdin.readline().rstrip()
secondString = sys.stdin.readline().rstrip()
thirdString = sys.stdin.readline().rstrip()
print(getLcs(firstString,secondString,thirdString))
