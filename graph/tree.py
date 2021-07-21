# 트리,1068번
import sys
sys.setrecursionlimit(10**6)
def dfs(curNode,deleteNode):
    cnt = 0
    if curNode==deleteNode:
        return 0
    for childNode in graph[curNode]:
        cnt +=dfs(childNode,deleteNode)
    if cnt==0:
        return 1
    return cnt

n = int(sys.stdin.readline().rstrip())
graph = [[]for _ in range(n)]
inputGraph = list(map(int,sys.stdin.readline().rstrip().split()))
deleteNode = int(sys.stdin.readline().rstrip())
start = 0
for childNode in range(n):
    if inputGraph[childNode] == -1:
        start=childNode
    else:
        parentNode = inputGraph[childNode]
        graph[parentNode].append(childNode)
print(dfs(start,deleteNode))