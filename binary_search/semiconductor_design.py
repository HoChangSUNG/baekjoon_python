# 반도체 설계, 2352번
import sys

def lower_bound(arr,target):
    low,high = 0,len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return low

n = int(sys.stdin.readline().rstrip())
sequence = list(map(int,sys.stdin.readline().split()))
lis=[]

for seq in sequence:
    if not lis or lis[-1]<seq:
        lis.append(seq)
    else:
        idx = lower_bound(lis,seq)
        lis[idx]=seq
print(len(lis))