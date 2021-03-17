from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solution(arr,row,col):  # 유기농 배추
    arr[row][col]=0
    queue = deque()
    queue.append((row,col))
    while queue:
        row,col = queue.popleft()
        for i in range(4):
            temp_row , temp_col = row+dr[i], col+ dc[i]
            if -1<temp_row<len(arr) and -1<temp_col<len(arr[0]):  # 인접 땅 확인해서 배추 심어져 있으면 0으로 변경
                if arr[temp_row][temp_col] == 1:
                    arr[temp_row][temp_col] = 0
                    queue.append((temp_row,temp_col))
    return 1

output = int(input())

for i in range(output):
    cnt = 0
    m, n, edge=map(int,input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)] # 땅의 값을 0으로 초기화

    for j in range(edge): # 배추가 심어져 있는 곳은 1로 변경
        m_, n_ = map(int,input().split())
        arr[n_][m_] = 1

    for w in range(n):
        for k in range(m):
            if arr[w][k] == 1:  # 배추가 심어져있을 경우
                cnt += solution(arr, w, k) # 현 위치의 배추와 인접한 배추들을 0으로 변경, 배추 흰지렁이 개수 +1

    print(cnt)