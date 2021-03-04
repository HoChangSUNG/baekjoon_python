from collections import deque
row, col = map(int,input().split())
arr = []
for i in range(row):
    col_element = list(map(int,input()))
    arr.append(col_element)

row_dir = [-1,0,1,0]
col_dir = [0,1,0,-1]
def solution(arr,row_len,col_len):  # 미로 탐색
    queue = deque()
    queue.append((0,0,1))
    visited = set((0,0))
    while queue:
        row,col,cnt = queue.popleft()
        if row == row_len-1 and col == col_len -1:
            print(cnt)
        for i in range(4):
            temp_row, temp_col = row+row_dir[i], col+col_dir[i]
            if -1 <temp_row<row_len and -1<temp_col<col_len and arr[temp_row][temp_col] == 1:
                if (temp_row,temp_col) not in visited:
                    queue.append((temp_row,temp_col,cnt+1))
                    visited.add((temp_row,temp_col))
solution(arr,row,col)