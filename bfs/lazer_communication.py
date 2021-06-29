# 레이저 통신, 6087번
import sys
from collections import deque
dr = [-1,0,1,0]
dc = [0,1,0,-1]
next_dir = [[0,1,3],[0,1,2],[1,2,3],[0,2,3]]
def bfs():
    queue = deque()
    visited = [[float('inf') for _ in range(w)] for _ in range(h)]
    for i in range(4): # 시작 위치에서 레이저 쏘는 위치,방향,거울 개수 저장
        queue.append(connect_point[0] + [i,0]) # 시작 row,시작 col,다음 방향,현재 거울 개수
    while queue:
        r,c,dir,cnt =queue.popleft() # row,col, dir, 거울 개수
        for i in next_dir[dir]:
            t_r,t_c,t_dir = r+dr[i],c+dc[i],i
            if -1<t_r<h and -1<t_c<w and lazer_map[t_r][t_c]!='*':
                t_cnt=cnt
                if dir!=t_dir: # 거울 설치후 90도 회전 시
                    t_cnt+=1
                if visited[t_r][t_c]>=t_cnt: #레이저가 이동해보야 하는 경우
                    queue.append([t_r,t_c,t_dir,t_cnt])
                    visited[t_r][t_c]=t_cnt
    return visited[connect_point[1][0]][connect_point[1][1]]

w,h = map(int,sys.stdin.readline().rstrip().split())
lazer_map = []
connect_point = []
for i in range(h):
    input =sys.stdin.readline().rstrip()
    temp = []
    for j in range(w):
        temp.append(input[j])
        if input[j]=='C':
            connect_point.append([i,j])
    lazer_map.append(temp)
print(bfs())