import sys
from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
arr = []
col, row = sys.stdin.readline().split()
for i in range(int(row)):
    arr.append(list(map(int, sys.stdin.readline().split())))

def solution(arr):  # 토마토
    ripe = 0  # 익은 토마토 개수
    empty = 0  # 비어있는 칸 개수
    date = 0   # 모든 토마토가 익는 최소날짜
    row_len = len(arr)
    col_len = len(arr[0])
    queue = deque()
    for i in range(row_len):
        for j in range(col_len):
            if arr[i][j] == 1:
                queue.append((i, j, 0))  #row,col,토마토 익는 날짜
            if arr[i][j] == -1:
                empty += 1
    while queue:
        row, col, cnt = queue.popleft()
        ripe += 1
        if cnt > date: # 현재 위치에서 토마토가 익는 날짜
            date = cnt
        for i in range(4): # 상하좌우 토마토 체크
            temp_row, temp_col = row+dr[i], col+dc[i]
            if -1<temp_row<row_len and -1<temp_col< col_len:
                if arr[temp_row][temp_col] == 0:  # 익지 않은 토마토일 경우
                    arr[temp_row][temp_col] = 1
                    queue.append((temp_row, temp_col, cnt+1))
    if ripe + empty == row_len*col_len: # 모든 토마토가 익은 경우
        return date
    else: # 익지 않은 토마토가 있는 경우
        return -1

print(solution(arr))