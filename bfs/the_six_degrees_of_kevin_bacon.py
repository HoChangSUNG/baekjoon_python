def solution(d): # 케빈 베이컨의 6단계 법칙, 플로이드 와샬
    for k in range(1,len(d)): # k 친구를 거쳐 지나가는 경우
        for i in range(1,len(d)):
            if i==k: # k와 같다면
                continue
            for j in range(1,len(d)):
                if j==k: # k와 같다면
                    continue
                if d[i][k] + d[k][j]<d[i][j]: # 거쳐 지나가는 경우가 거리가 더 짧다면
                    d[i][j] = d[i][k] + d[k][j]
    min = sum(d[1][1:]) # 1번 친구의 케빈 베이컨의 수 기준
    num = 1 # 1번 친구
    for i in range(1,len(d)):
        if min>sum(d[i][1:]): # i번 친구의 케빈 베이컨의 수가 더 작다면
            min = sum(d[i][1:])
            num = i
    return num # 케빈 베이컨의 수가 가장 작은 사람 반환

N, M = map(int,input().split())
d = [[float('INF') for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    d[i][i] = 0
for i in range(M):
    a,b = map(int,input().split())
    d[a][b], d[b][a] = 1, 1
print(solution(d))

