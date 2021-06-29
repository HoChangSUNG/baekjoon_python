from collections import deque
# 0->동 1->서 2->남 3->북
go_r = [0,0,1,-1]  # 해당 방향에서 직진할 때 row, col값
go_c = [1,-1,0,0]
dir = { # 해당 방향에서 오른쪽, 왼쪽으로 90도 회전
    0:[2,3],  # 동쪽에서 오른쪽으로 90도 회전(남), 왼쪽으로 90도 회전(북)
    1:[3,2],
    2:[1,0],
    3:[0,1]
}
def bfs(s_r,s_c,s_d,e_r,e_c,e_d,visited,robot_map):
    queue = deque()
    queue.append([s_r,s_c,s_d]) # 초기값
    visited[s_d][s_r][s_c] = 0
    while queue:
        r,c,d = queue.popleft()
        if r == e_r and c == e_c and d == e_d: # 도착지점에 도착할 경우
            return visited[d][r][c]
        # 명령1:GO k, k는 1,2,3 현재 방향으로 k 만큼 이동
        for i in range(1,4): # 1~3 만큼 각각 이동
            t_r,t_c = r+go_r[d]*i, c+go_c[d]*i # i만큼 해당 방향으로 이동
            if t_r<0 or t_r>=len(robot_map) or t_c<0 or t_c>=len(robot_map[0]) or robot_map[t_r][t_c] == 1:
                break # 벽이거나 범위를 넘어서면 다음 루프는 어짜피 범위를 넘거나 벽에 막히기 때문에 다음 루프 실행할 필요 x
            if visited[d][t_r][t_c]==-1:
                visited[d][t_r][t_c] = visited[d][r][c]+1
                queue.append([t_r,t_c,d])
        # 명령2:Turn left or right. 각각 왼쪽 또는 오른쪽으로 90도 회전 0 -> 오른쪽, 1 ->왼쪽
        for i in range(2):
            t_d = dir[d][i] # 90도 회전한 dir
            if visited[t_d][r][c] == -1:
                visited[t_d][r][c] = visited[d][r][c]+1
                queue.append([r,c,t_d])
    return -1 # 도착지점에 도착하지 못하는 경우
m,n = map(int,input().split())
robot_map = [list(map(int,input().split()))for i in range(m)]
visited = [[[-1 for _ in range(n)]for _ in range(m)]for _ in range(4)] # 각각의 방향에 따른 방문 여부 확인
s_r,s_c,s_d = map(int,input().split())
e_r,e_c,e_d = map(int,input().split())
print(bfs(s_r-1,s_c-1,s_d-1,e_r-1,e_c-1,e_d-1,visited,robot_map))