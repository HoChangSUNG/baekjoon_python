from collections import deque
dr=[-1,0,1,0]
dc=[0,1,0,-1]
baby=[]  # 아기상어의 위치
food_cnt = 0  # 물고기 개수
baby_size = 2  # 아기 상어 크기
baby_eat = 0  # 아기 상어가 먹은 물고기 수
total_time = 0  # 물고기를 잡아먹는데 쓰는 시간
def eat_food_bfs(game_map,baby_row,baby_col):  # 아기상어, 아기 상어가 물고기를 잡아먹는 경우
    global food_cnt
    global baby_size
    global baby_eat
    global baby
    can_eat=[] # 아기 상어가 먹을 수 있는 물고기들
    min_time = -1
    visited = set() # 아기상어가 방문한 곳
    visited.add((baby_row,baby_col))
    queue = deque()
    queue.append([baby_row,baby_col,0]) # 아기상어 위치, 걸린 시간
    while queue:
        row,col,time = queue.popleft() # 아기 상어 위치,해당 위치까지 오는데 걸린 시간
        # print(row,col,time)
        # print("최소시간,현재시간",min_time,time)
        if min_time==time: # 먹을 수 있는 물고기가 1마리 이상일 때 물고기를 먹는 경우
            # print("min_time",time)
            eat = sorted(can_eat,key = lambda item:(item[0],item[1]))[0] # 먹을 수 있는 물고기들중 가장 가까운 물고기 선별
            baby_eat+=1

            if baby_size==baby_eat: # 물고기 크기 증가하는 경우
                baby_size+=1
                baby_eat=0
            game_map[eat[0]][eat[1]]=0
            food_cnt-=1
            baby=eat # 현재 아기 상어 위치 최신화
            return time  # 물고기 먹었을 때 시간 반환
        for i in range(4):
            temp_row,temp_col = row+dr[i], col+dc[i]
            if (temp_row,temp_col) not in visited and -1<temp_row<len(game_map) and -1<temp_col<len(game_map):
                if game_map[temp_row][temp_col]<=baby_size: # 아기상어가 이동하거나 먹을 수 있는 경우
                    visited.add((temp_row,temp_col))
                    if game_map[temp_row][temp_col]==baby_size or game_map[temp_row][temp_col]==0: # 아기상어가 이동만 하는 경우
                        queue.append(([temp_row,temp_col,time+1]))
                    else: # 아기상어가 이동할 수 있고 먹을 수 있는 경우
                        queue.append(([temp_row, temp_col, time + 1]))
                        min_time=time+1
                        can_eat.append([temp_row,temp_col])
                        # print("최소시간", min_time)
                        # print(can_eat)

    return 0  # 물고기를 먹지 못해 엄마 상어에게 도움을 요청해야 하는 경우
length = int(input())
game_map  = [list(map(int, input().split())) for _ in range(length)]
# print(game_map)
for i in range(length):
    for j in range(length):
        if 0<game_map[i][j]<7:
            food_cnt+=1
        if game_map[i][j]==9:
            game_map[i][j]=0
            baby = [i,j]
while food_cnt>0: # 먹을 수 있는 물고기가 남아있는 경우
    check = eat_food_bfs(game_map,baby[0],baby[1])
    if check==0:  # 물고기를 먹지 못해 엄마 상어에게 도움을 요청해야 하는 경우
        break
    total_time+=check # 아기 상어가 물고기를 먹는 동안 걸린 시간
print(total_time)
