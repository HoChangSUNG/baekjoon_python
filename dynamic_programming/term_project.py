import sys
sys.setrecursionlimit(10**8)
# 텀 프로젝트, 9466번
def dfs(n):
    if n in cycle: #팀이 만들어졌을 경우
        visited[n]+=1
        cycle_start = n
        while arr[cycle_start]!=n:
            visited[arr[cycle_start]]+=1 #팀이 만들어졌을 경우 표시
            cycle_start=arr[cycle_start]

        return
    else:
        if visited[n]==0: # 방문하지 않은 경우
            visited[n]+=1 # 방문했다고 표시
            cycle.add(n)

            dfs(arr[n])
        else: # 방문한 경우
            return
t = int(sys.stdin.readline())
for _ in range(t):
    graph = {}
    n = int(sys.stdin.readline())
    arr = [0]+list(map(int,sys.stdin.readline().rstrip().split()))
    visited = [0]*(len(arr)+1)
    for i in range(1,len(arr)):
        cycle = set()
        if visited[i]==0 :
            dfs(i)
    print(visited.count(1)) # 2는 team에 속한 학생들, 1은 팀에 속하지 않은 학생들-> 1의 개수 찾기 -> 팀에 속하지 않은 학생 수