# 꼬인 전깃줄, 1365번
import sys
from bisect import bisect_left
def lowerBound(target):
    low = 0
    high = len(lis)-1
    while low<=high:
        mid = (low+high)//2
        if lis[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return low
n = int(sys.stdin.readline().rstrip())
wires = list(map(int, sys.stdin.readline().rstrip().split()))
lis = []
for wire in wires:
    if len(lis)==0 or lis[-1]<wire:
        lis.append(wire)
    else:
        lis[lowerBound(wire)] = wire
        # lis[bisect_left(lis, pole)]=pole

print(n -len(lis))
