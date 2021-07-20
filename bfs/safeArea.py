# 안전영역, 2468번
import sys
from collections import deque
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def safeAreaCnt(area,height):
    cnt = 0
    visited = [[False for _ in range(len(area))]for _ in range(len(area))]
    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j]>height and not visited[i][j]:
                bfs(area,visited,height,i,j)
                cnt+=1
    return cnt
def bfs(area,visited,height,i,j):
    visited[i][j]=True
    queue = deque()
    queue.append([i,j])
    while queue:
        row,col = queue.popleft()
        for i in range(4):
            next_row,next_col = row+dr[i],col+dc[i]
            if -1< next_row<len(area) and -1 < next_col <len(area):
                if area[next_row][next_col]>height and not visited[next_row][next_col]:
                    queue.append([next_row,next_col])
                    visited[next_row][next_col]=True

n = int(sys.stdin.readline().rstrip())
area = []
maxHeight = 0
for _ in range(n):
    a = list(map(int,sys.stdin.readline().rstrip().split()))
    maxHeight = max(maxHeight,max(a))
    area.append(a)
cnt = 1
for h in range(1,maxHeight):
    cnt = max(cnt,safeAreaCnt(area,h))
print(cnt)