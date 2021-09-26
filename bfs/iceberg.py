# 빙산, 2573번
import sys
from collections import deque

dr=[-1,0,1,0]
dc=[0,1,0,-1]
def meltingIce(i,j):
    queue= deque()
    queue.append([i,j])
    visited[i][j]=True

    while(queue):
        row,col = queue.popleft()
        for i in range(4):
            tmpRow,tmpCol = row+dr[i],col+dc[i]
            if -1<tmpRow<n and -1<tmpCol<m:
                if maps[tmpRow][tmpCol]==0 and not visited[tmpRow][tmpCol]:
                    queue.append([tmpRow,tmpCol])
                    visited[tmpRow][tmpCol]=True
                if maps[tmpRow][tmpCol] != 0:
                    maps[tmpRow][tmpCol]-=1
                    if maps[tmpRow][tmpCol]==0:
                        visited[tmpRow][tmpCol]=True

def countIceberg(i,j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            tmpRow, tmpCol = row + dr[i], col + dc[i]
            if -1 < tmpRow < n and -1 < tmpCol < m:
                if maps[tmpRow][tmpCol]!=0 and not visited[tmpRow][tmpCol]:
                    queue.append([tmpRow, tmpCol])
                    visited[tmpRow][tmpCol]=True

n,m=map(int,sys.stdin.readline().rstrip().split())
maps =[]
for _ in range(n):
    maps.append(list(map(int,sys.stdin.readline().rstrip().split())))

islandCnt=1
year=0
while(islandCnt==1):
    curIslandCnt = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j]==0 and not visited[i][j]:
                meltingIce(i,j)# 빙산 녹이기

    for i in range(n):
        for j in range(m):
            if maps[i][j]!=0 and not visited[i][j]:
                countIceberg(i,j)# 빙산 개수 확인
                curIslandCnt+=1
    year+=1
    islandCnt=curIslandCnt

if islandCnt==0:
    print(0)
else:
    print(year)