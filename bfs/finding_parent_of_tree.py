from collections import deque

def solution(graph):  # 트리의 부모 찾기
    parents = [i for i in range(len(graph) + 1)]  # 해당 노드의 부모
    visited = set()
    visited.add(1)
    queue = deque()
    queue.append(1)  # 루트 노드인 1부터 시작
    while queue:
        node = queue.popleft()
        for adgacent_node in graph[node]:
            if adgacent_node not in visited:
                parents[adgacent_node] = node
                visited.add(adgacent_node)
                queue.append(adgacent_node)
    for parent in parents[2:]:  # 2부터 부모 노드를 출력
        print(parent)


N = int(input())
graph = {i: [] for i in range(1, N + 1)}
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
solution(graph)
