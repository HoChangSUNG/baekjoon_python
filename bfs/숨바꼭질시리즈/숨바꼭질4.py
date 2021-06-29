from collections import deque
def bfs(start,target,visited):  # 숨바꼭질 4
    queue =deque()
    queue.append(start)
    visited[start] = start
    while queue:
        loc = queue.popleft()
        if loc == target:
            return
        for t_loc in (loc+1,loc-1,loc*2):
            if 0<=t_loc<=100000:
                if visited[t_loc] == -1:
                    visited[t_loc] = loc
                    queue.append(t_loc)
s, t = map(int,input().split())
visited = [-1 for _ in range(100001)]
bfs(s,t,visited)
a = t
answer = ""
cnt = 0
while a!=visited[a]:
    cnt+=1
    answer = str(a)+" "+ answer
    a = visited[a]
print(cnt)
print(str(s)+" "+answer)