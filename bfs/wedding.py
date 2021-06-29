from collections import deque
def solution(graph):  # 결혼식
    visited = [-1 for _ in range(len(graph)+1)]
    queue = deque()
    queue.append(1)
    visited[1] = 0
    while queue:
        node = queue.popleft()
        for adjacent_node in graph[node]:
            if visited[adjacent_node]==-1: # 방문하지 않았울 경우
                n_visited = visited[node] + 1
                if n_visited<=2: # 친구의 친구까지만 탐색
                    visited[adjacent_node] =n_visited
                    queue.append(adjacent_node)
    return visited.count(1)+visited.count(2) # 친구,친구의 친구 수 리턴

n =int(input())
m = int(input())
graph = {i:[] for i in range(1,m+1)}
for i in range(m):
    a,b  = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(solution(graph))
