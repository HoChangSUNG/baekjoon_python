 #  욕심쟁이 판다 1937번
import sys
sys.setrecursionlimit(40000)
dr, dc=[-1,0,1,0],[0,1,0,-1]
n = int(input())
forest = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
def dfs(r,c):
    temp=0
    if dp[r][c]!=0:
        return dp[r][c]
    dp[r][c] = 1
    for i in range(4):
        t_r,t_c = r+dr[i],c+dc[i]
        if -1<t_r<n and -1<t_c<n:
            if forest[r][c]<forest[t_r][t_c]:
                temp = max(temp,dfs(t_r,t_c))
    dp[r][c] += temp
    return dp[r][c]
answer = 1
for i in range(n):
    for j in range(n):
        if dp[i][j] ==0:
            dfs(i,j)

print(max(map(max,dp)))