from collections import deque
dy = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def solution(row,col):  # 영역 구하기
    area_cnt = 0
    queue = deque()
    queue.append((row,col))
    arr[row][col] = 0
    while queue:
        row,col = queue.popleft()
        area_cnt +=1
        for i in range(4):
            temp_row,temp_col = row+dy[i],col+dc[i]
            if -1<temp_row<len(arr) and -1<temp_col<len(arr[0]):
                if arr[temp_row][temp_col] == 1:
                    queue.append((temp_row,temp_col))
                    arr[temp_row][temp_col]=0
    return area_cnt

row_len,col_len,rectangle = map(int,input().split()) #  입력
arr = [[1 for _ in range(col_len)]for _ in range(row_len)]
for i in range(rectangle):
    start_x,start_y,end_x,end_y = map(int,input().split())
    for y in range(start_y,end_y):
        for x in range(start_x,end_x):
            arr[y][x] = 0
# print(arr)
area = []
area_cnt = 0
for i in range(len(arr)):  # 영역 탐색
    for j in range(len(arr[0])):
        if arr[i][j] == 1:
            area.append(solution(i,j))
            area_cnt += 1
print(area_cnt)
area.sort()
print(' '.join(list(map(str,area))))