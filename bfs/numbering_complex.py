from collections import deque
arr_len =int(input())
arr = []
for i in range(arr_len):
    arr.append(list(map(int,input())))
visited = set()

for i in range(len(arr)): # 집이 있는 위치를 visited에 넣어주기, 집이 있는 위치만 탐색하면 끝.
    for j in range(len(arr)):
        if arr[i][j] == 1:
            visited.add((i,j))
dy = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def solution(complex):  # 단지 번호 붙이기
    queue = deque()
    answer = []
    cnt = 0
    queue.append((complex.pop()))
    while True:
        if len(queue)==0: # 인접한 집이 없을때
            answer.append(cnt)
            cnt = 0
            if len(complex)==0:  # 모든 집을 방문한 경우
                return answer  # 단지에 속하는 집의 수 반환
            else: # 다른 단지가 존재하는 경우
                queue.append(complex.pop())
        row,col = queue.popleft() # 집 위치
        cnt+=1 # 집 개수 세기
        for i in range(4): # 인접한 집 탐색
            temp_row,temp_col = row + dy[i], col + dc[i]
            if (temp_row,temp_col) in visited:
                queue.append((temp_row,temp_col))
                visited.remove((temp_row,temp_col))
complex = solution(visited)
complex.sort() #  출력 부분
print(len(complex))
for i in range(len(complex)):
    print(complex[i])
