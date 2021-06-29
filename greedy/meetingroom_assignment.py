# 회의실 배정, 1931번
import sys

n = int(sys.stdin.readline())
time = []
for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().rstrip().split())))
time.sort(key=lambda x: (x[1], x[0]))

meeting_end = 0
cnt = 0
for cur_start, cur_end in time:
    if cur_start >= meeting_end:
        cnt += 1
        meeting_end = cur_end

print(cnt)
