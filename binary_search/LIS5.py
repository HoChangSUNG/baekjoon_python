# 가장 긴 증가하는 부분 수열5, 14003번
import sys
from bisect import bisect_left

n = int(sys.stdin.readline().rstrip())
sequence = list(map(int,sys.stdin.readline().rstrip().split()))

lis = []
backtracking = [-1] * len(sequence)
maxLen = 0
for i in range(len(sequence)):
    if len(lis) == 0 or lis[-1] < sequence[i]:
        lis.append(sequence[i])
        backtracking[i]=maxLen
        maxLen+=1
    else:
        index = bisect_left(lis,sequence[i])
        lis[index] = sequence[i]
        backtracking[i]=index
print(maxLen)

result = [0]*maxLen
maxLen-=1
for i in range(n-1,-1,-1):
    if backtracking[i]==maxLen:
        result[maxLen]=sequence[i]
        maxLen -= 1
print(*result)
