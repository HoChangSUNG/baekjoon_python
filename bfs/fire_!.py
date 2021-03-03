from collections import deque
dr,dc = [-1,0,1,0],[0,1,0,-1]
def bfs(maps,fire,loc):  # 불!
    queue = deque()
    for i in range(len(fire)):
        queue.append(fire[i])
    queue.append(loc)
    while queue:
        r,c,t = queue.popleft() # row,col,불인지 지훈이 이동 횟수인지
        if t!=-1 and (r==0 or r ==len(maps)-1 or c==0 or c==len(maps[0])-1): # 지훈이가 미로 가장자리에 위치할 때
            return t+1
        for i in range(4):
            t_r,t_c = r+dr[i],c+dc[i]
            if 0>t_r or t_r>=len(maps) or 0>t_c or t_c>=len(maps[0]) or maps[t_r][t_c] == 'F' or maps[t_r][t_c]=="#":
                continue
            if t == -1: # 불이 번질 때
                queue.append([t_r,t_c,t])
                maps[t_r][t_c] = 'F'
            if maps[t_r][t_c] =='.': # 지훈이가 해당 위치를 방문하지 않았을 경우
                queue.append([t_r,t_c,t+1])
                maps[t_r][t_c]='..' # 방문여부 변경
    return 'IMPOSSIBLE'
maps = []
fire = [] # 불 우치
loc = [] # 지훈이 위치
r,c = map(int,input().split())
for i in range(r):
    maps.append(list(input()))
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'J':
            loc = [i, j, 0]  # 시작 위치
            maps[i][j] = '.'
        if maps[i][j] == 'F': # 불 위치
            fire.append([i, j, -1])
print(bfs(maps,fire,loc))