from collections import deque
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def solution(maps,s_loc,fire):  # 불
    queue = deque()
    for i in range(len(fire)):
        queue.append(fire[i])
    queue.append(s_loc)

    while queue:
        row,col,cnt = queue.popleft()
        for i in range(4):
            temp_row,temp_col = row +dr[i], col + dc[i]
            if -1<temp_row<len(maps) and -1<temp_col<len(maps[0]) :
                if maps[temp_row][temp_col] != '#':
                    if maps[temp_row][temp_col] != '*': # 불의 확산
                        if cnt == -1:
                            maps[temp_row][temp_col]="*"
                            queue.append([temp_row,temp_col,-1])
                        elif cnt != -1 and maps[temp_row][temp_col] == '.': # 사람이 이동 가능할때
                            maps[temp_row][temp_col] = '..'
                            queue.append([temp_row, temp_col,cnt+1])
            if (not(-1<temp_row<len(maps)) or not (-1<temp_col<len(maps[0]))) and cnt!= -1 : # 사람이 탈출할때
                return cnt+1
    return 'IMPOSSIBLE' # 탈출 불가능
loop = int(input())
for i in range(loop):
    maps = []
    fire = []
    loc = []
    a,b = map(int,input().split())
    for j in range(b):
        maps.append(list(input()))
    for j in range(b):
        for k in range(a):
            if maps[j][k] == '@':
                loc = [j,k,0]
                maps[j][k] = '.'
            if maps[j][k] == '*':
                fire.append([j,k,-1])
    print(solution(maps,loc,fire))

