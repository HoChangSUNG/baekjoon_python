from collections import deque
dr, dc = [-1,0,1,0],[0,1,0,-1]
def bfs(picture,answer,i,j):  # 그림
    queue = deque()
    queue.append([i,j])
    picture[i][j] = 0
    cnt = 1 # 그림 넓이
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            t_r, t_c = r+dr[i],c+dc[i]
            if t_r<0 or t_r>=len(picture) or t_c<0 or t_c>=len(picture[0]) or picture[t_r][t_c] == 0:
                continue
            cnt+=1
            queue.append([t_r,t_c])
            picture[t_r][t_c] = 0
    answer.append(cnt) # 그림 넓이 저장
    return
n,m = map(int,input().split())
picture = []
answer = []
for i in range(n):
    picture.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            bfs(picture,answer,i,j)
if answer:
    an = sorted(answer,reverse=True)
    print(len(an))
    print(an[0])
else: # 그림이 하나도 없을 경우
    print(0)
    print(0)