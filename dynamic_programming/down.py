 #  내리막길 1520번
import sys
dr,dc = [-1,0,1,0],[0,1,0,-1]
m,n = map(int, sys.stdin.readline().split())
path = []
for _ in range(m):
    path.append(list(map(int,sys.stdin.readline().split())))
dp = [[-1]*n for _ in range(m) ]

def dfs(r,c):
    if r==m-1 and c==n-1:
        return 1
    if dp[r][c]==-1:
        dp[r][c] = 0
        for i in range(4):
            t_r,t_c = r+dr[i],c+dc[i]
            if -1<t_r<m and -1<t_c<n and path[r][c]>path[t_r][t_c]:
                dp[r][c] += dfs(t_r,t_c)
    return dp[r][c]


print(dfs(0,0))
