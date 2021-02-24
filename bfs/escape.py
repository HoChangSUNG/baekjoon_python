from collections import deque
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def bfs(area,S_loc,D_loc,W_loc):  # 탈출
    # print(D_loc, W_loc)
    queue = deque() # 위치,물(-1)/고슴도치(0이상) 이동 구분
    for i in range(len(W_loc)):  # 물 위치(row,col,-1) -> -1은 물이라는 표시
        queue.append(W_loc[i])
    queue.append(S_loc) # 고슴도치 현재 위치(row,col,time)
    while queue:
        row,col,time = queue.popleft()
        # print(row,col,cnt)
        if row == D_loc[0] and col == D_loc[1]: # 비버 소굴 도착시
            return time
        for i in range(4):
            temp_row, temp_col = row+dr[i],col+dc[i]
            if -1<temp_row<len(area) and -1<temp_col<len(area[0]):
                if time == -1:  # 물이 확장되는 경우
                    if area[temp_row][temp_col] =='.' or area[temp_row][temp_col] =='..': # 장애물,비버 소굴이 아닐 경우
                        area[temp_row][temp_col] = '*'
                        queue.append([temp_row,temp_col,-1])
                else:  # 고슴도치 이동
                    if area[temp_row][temp_col] =='.' or area[temp_row][temp_col] =='D': # 방문하지 않은 위치,비버 소굴로 이동시
                        area[temp_row][temp_col] = '..' # 고슴도치가 방문했다고 표시
                        queue.append([temp_row,temp_col,time+1])

    return 'KAKTUS'  # 비버 소굴 도착 불가능할 경우

D_loc = [] # 비버 소굴
S_loc = [] # 고슴도치 위치
W_loc = [] # 물 위치
R,C = map(int, input().split())
area = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if area[i][j]=='S':
            S_loc = [i,j,0]
            area[i][j] = '.'
        if area[i][j] == 'D':
            D_loc = [i, j]
        if area[i][j] == '*':
            W_loc.append([i,j,-1])

print(bfs(area,S_loc,D_loc,W_loc))