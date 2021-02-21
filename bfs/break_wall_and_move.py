from collections import deque
dr=[-1,0,1,0]
dc=[0,1,0,-1]
def solution(row_len,col_len,game_map):  # 벽 부수고 이동하기
    queue = deque()
    queue.append((0,0,0,1)) # 현재 row,col,벽뚫은거 유무,cnt
    visited = set() # 벽을 부수지 않은 상태에서 방문한 곳
    visited_wall =set() # 벽을 부수고 방문한 곳
    visited.add((0,0))
    visited_wall.add((0,0))
    while queue:
        row,col,wall,cnt = queue.popleft()
        # print(row,col,wall,cnt)
        if row==row_len-1 and col == col_len-1: # 목적지에 도착했을 때 최단 경로
            return cnt
        for i in range(4):
            temp_row,temp_col = row+dr[i],col+dc[i]
            if -1<temp_row<row_len and -1<temp_col<col_len: # 다음 이동할 곳이 맵 내에 위치할 때
                if wall==0: # 벽을 한번도 부수지 않은 경우
                    if game_map[temp_row][temp_col]==0 and (temp_row,temp_col) not in visited:  # 방문하지 않고 이동이 가능하다면
                        visited.add((temp_row,temp_col))
                        queue.append((temp_row,temp_col,wall,cnt+1))
                    elif game_map[temp_row][temp_col]==1 and (temp_row,temp_col) not in visited_wall:  # 벽을 뚫을 경우
                        visited_wall.add((temp_row, temp_col))
                        queue.append((temp_row, temp_col, wall+1, cnt + 1))
                else:  # 벽을 1번 부순경우
                    if game_map[temp_row][temp_col]==0 and (temp_row,temp_col) not in visited_wall:  #  벽을 더이상 뚫지 못하고 이동만 할 수 있는 경우
                        visited_wall.add((temp_row,temp_col))
                        queue.append((temp_row,temp_col,wall,cnt+1))


    return -1  # 목적지에 도착하지 못하는 경우

row_len ,col_len = map(int,input().split())
game_map=[]
for i in range(row_len):
    game_map.append(list(map(int,input())))
print(solution(row_len,col_len,game_map))