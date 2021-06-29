 # 점프 1890번
import sys
dr, dc = [0, 1],[1, 0]
n = int(input())
game = [list(map(int,sys.stdin.readline().rstrip().split()))for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
def dfs(r, c):
    if r == n-1 and c == n-1:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0
    for i in range(2):
        t_r, t_c = r + dr[i]*game[r][c], c+dc[i]*game[r][c]
        if -1 < t_r < n and -1 < t_c < n:
            dp[r][c] += dfs(t_r, t_c)
    return dp[r][c]
print(dfs(0, 0))

