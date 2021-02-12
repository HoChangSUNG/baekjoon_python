from collections import deque

def solution(graph,start_node,end_node):  # 촌수 계산
    visited = set()
    visited.add(start_node)
    queue = deque()
    queue.append((start_node,0)) # 노드, 촌수

    while queue: # bfs
        node,cnt = queue.popleft()
        if node == end_node:
            return cnt
        for adjacent_node in graph[node]:
            if adjacent_node not in visited:
                queue.append((adjacent_node,cnt+1))
                visited.add(adjacent_node)
    return -1

n = int(input()) # 전체 사람 수
num_1, num_2 = map(int,input().split()) # 촌수 계산해야 하는 두 사람의 번호(1...n)
m = int(input()) # 부모 자식 관계 개수
graph={i:[] for i in range(1, n + 1)}
for i in range(m):
    x, y = map(int, input().split()) #부모,자식 관계
    graph[x].append(y)
    graph[y].append(x)
print(solution(graph, num_1, num_2))

