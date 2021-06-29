 #  구간 합 구하기4, 11659번
import sys

n, m =map(int, sys.stdin.readline().rstrip().split())

data = list(map(int,sys.stdin.readline().rstrip().split()))
prefix_sum = [0]
sum_value = 0
for i in data:
    sum_value+=i
    prefix_sum.append(sum_value)

for i in range(m):
    left,right = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[right]-prefix_sum[left-1])