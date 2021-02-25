from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def solution(i,j,color,arr): # 구역의 범위를 확인, 적록색약
    queue = deque()
    queue.append((i,j)) # 시작 위치
    arr[i][j] = 'W' # 확인했으면 흰색으로 변경
    while queue:
        row,col = queue.popleft()
        for i in range(4):
            temp_r, temp_c= row + dr[i], col+dc[i]
            if -1<temp_r<len(arr) and -1<temp_c<len(arr):
                if arr[temp_r][temp_c] == color: # 구역의 범위 안쪽일 경우
                    queue.append((temp_r,temp_c))
                    arr[temp_r][temp_c] = 'W'  # 확인했으면 흰색으로 변경
    return

num = int(input())
normal = []  # 적록색약이 아닌 사람이 본 색상들
abnormal = [[] for _ in range(num)] # 적록색약인 사람이 본 색상들
for i in range(num): # 적록색약이 아닌 사람이 본 색상들
    normal.append(list(input()))
for i in range(num):
    for j in range(num): # 적록색약인 사람이 본 색상들
        if normal[i][j] == 'R':  # R을 G로 취급하기
            abnormal[i].append('G')
        else:
            abnormal[i].append(normal[i][j])

normal_cnt, abnormal_cnt = 0, 0  #  적록색약이 아닌 사람이 봤을 때 구역의 수, 적록색약인 사람이 봤을 때 구역의 수
for i in range(num):
    for j in range(num):
        if normal[i][j] != 'W':  # 적록색약이 아닌 사람이 봤을 때 다른 색깔의 구역인 경우
            solution(i,j,normal[i][j],normal)
            normal_cnt+=1
        if abnormal[i][j] != 'W': # 적록색약인 사람이 봤을 때 다른 색깔의 구역인 경우
            solution(i, j, abnormal[i][j], abnormal)
            abnormal_cnt += 1
print(normal_cnt,abnormal_cnt)