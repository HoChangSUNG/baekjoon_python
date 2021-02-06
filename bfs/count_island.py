from collections import deque
dr = [[-1,0,1,0],[-1,-1,1,1]]  # 상하좌우, 대각선
dc = [[0,1,0,-1],[-1,1,1,-1]]  # 상하좌우, 대각선
def bfs(row,col): #  섬의 개수
    queue =deque()
    queue.append((row,col))
    arr[row][col]=0
    while queue:
        row,col = queue.popleft()
        for i in range(2): # 인접한 상하좌우,대각선 탐색
            for j in range(4):
                temp_row,temp_col = row+dr[i][j], col+dc[i][j]
                if -1<temp_row<len(arr) and -1<temp_col<len(arr[0]):
                    if arr[temp_row][temp_col] == 1:
                        queue.append((temp_row,temp_col))
                        arr[temp_row][temp_col] = 0
    return 1

while True:
    w,h = map(int,input().split())
    arr=[]
    cnt=0

    if w==0 and h==0:
        break
    for _ in range(h):
        arr.append(list(map(int,input().split())))

    for i in range(h):
        for j in range(w):
            if arr[i][j]==1:
                cnt += bfs(i,j)

    print(cnt)