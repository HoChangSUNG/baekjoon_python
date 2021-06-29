from collections import deque
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def solution(maps,i,j):  # 보물섬
    queue =deque()
    queue.append((i,j))
    visited = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))] # 방문 및 걸린 시간
    visited[i][j] +=1 # 시작 위치 ->시간 : 0
    cnt = 0
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            temp_row, temp_col  = row+dr[i], col +dc[i]
            if -1<temp_row<len(maps) and -1<temp_col<len(maps[0]):
                if maps[temp_row][temp_col] == 'L' and visited[temp_row][temp_col] == -1: # 육지이고 한번도 방문 안했을 경우
                    queue.append((temp_row,temp_col))
                    visited[temp_row][temp_col] = visited[row][col] + 1 # 걸린 시간 +1
                    cnt = max(cnt,visited[temp_row][temp_col]) # 매 queue 마다 시간 비교
    return cnt

maps = []
cnt = 0
row,col = map(int,input().split())
for i in range(row):
    maps.append(list(input()))
for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j] == 'L': # 모든 육지에서 가장 멀리 떨어진 곳에 도달하느 시간 리턴
            cnt = max(cnt,solution(maps,i,j)) # 큰 수 사용
print(cnt)