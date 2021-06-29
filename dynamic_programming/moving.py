 #  이동하기, 11048번
import sys
def solution(maze,n,m):
    dp=[[0 for _ in range(m)]for _ in range(n)]
    dp[0][0] = maze[0][0]
    for i in range(1,m): # 0번째 행 최대값 저장
        dp[0][i] = dp[0][i-1] +maze[0][i]
    for i in range(1,n): # 0번째 열 최대값 저장
        dp[i][0] = dp[i-1][0]+maze[i][0]
    for i in range(1,n): # 이동시 최대값
        for j in range(1,m):
            dp[i][j] = max(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+maze[i][j]
    return dp[n-1][m-1]

maze = []
n,m = map(int,sys.stdin.readline().rstrip().split())
for _ in range(n):
    maze.append(list(map(int,sys.stdin.readline().rstrip().split())))
print(solution(maze,n,m))