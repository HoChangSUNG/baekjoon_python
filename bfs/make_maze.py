from queue import PriorityQueue
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def bfs(maze):  #  미로 만들기
    que = PriorityQueue()
    que.put((0,0,0))
    visited = [[0 for _ in range(len(maze))]for _ in range(len(maze))] # 방문 여부 확인
    visited[0][0] = 1
    while not que.empty():
        cnt,r,c = que.get()
        # print(cnt,r,c)
        if r == len(maze)-1 and c == len(maze) - 1 :
            return cnt
        for i in range(4):
            temp_r,temp_c = r +dr[i], c+dc[i]

            if -1<temp_r<len(maze) and -1< temp_c<len(maze) and visited[temp_r][temp_c]==0:
                if maze[temp_r][temp_c] ==1: # 흰방일 경우
                    que.put((cnt,temp_r,temp_c))
                    visited[temp_r][temp_c] =1
                elif maze[temp_r][temp_c] ==0: # 검은방일 경우
                    que.put((cnt+1, temp_r, temp_c))
                    visited[temp_r][temp_c] = 1
n = int(input())
maze = []
for i in range(n):
    maze.append(list(map(int,list(input()))))

print(bfs(maze))