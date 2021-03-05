from collections import deque
dr_m = [-1,0,1,0]
dc_m = [0,1,0,-1]
dr_h = [-1,-2,-2,-1,1,2,2,1]
dc_h = [-2,-1,1,2,-2,-1,1,2]
def bfs(chess_map,max_k):  # 말이 되고픈 원숭이
    visited = [[[-1 for _ in range(w)] for _ in range(h)] for _ in range(max_k + 1)]  # 말의 움직임을 포함한 원숭이의 방문 여부
    queue = deque()
    queue.append([0,0,0])  # 좌표, k
    visited[0][0][0] = 0
    while queue:
        r,c,k = queue.popleft() # row,col,k(말의 움직임 횟수)

        if r == len(chess_map)-1 and c == len(chess_map[0])-1: # 목적지에 도착
            return visited[k][r][c]

        for i in range(8): # 말의 움직임
            t_r,t_c,t_k = r+dr_h[i], c+dc_h[i],k+1
            if -1<t_r<len(chess_map) and -1<t_c<len(chess_map[0]) and t_k<=max_k and chess_map[t_r][t_c]=='0':
                if visited[t_k][t_r][t_c] == -1:
                    visited[t_k][t_r][t_c] = visited[k][r][c] + 1
                    queue.append([t_r,t_c,t_k])

        for i in range(4): # 원숭이의 움직임
            t_r,t_c = r+dr_m[i], c+dc_m[i]
            if -1 < t_r < len(chess_map) and -1 < t_c < len(chess_map[0]) and chess_map[t_r][t_c]=='0':
                if visited[k][t_r][t_c] == -1:
                    visited[k][t_r][t_c] = visited[k][r][c] + 1
                    queue.append([t_r, t_c, k])
    return -1  # 목적지에 도착 불가
k = int(input())
w, h = map(int,input().split())
chess_map = []
for i in range(h):
    chess_map.append(list(input().split()))

print(bfs(chess_map,k))
