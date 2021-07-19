# 가장 긴 증가하는 부분 수열2, 12015번
import sys
from bisect import bisect_left

n = int(sys.stdin.readline().rstrip())
sequence = list(map(int,sys.stdin.readline().rstrip().split()))
def lis(sequence):
    lis = []
    for seq in sequence:
        if len(lis) == 0 or lis[-1] < seq:
            lis.append(seq)
        else:
            index = lowerBound(lis, seq)
            lis[index] = seq
    return len(lis)
def lowerBound(array,target):
    low = 0
    high = len(array)-1
    index = -1
    while low<=high:
        mid = (low+high)//2
        if array[mid]<target:
            low=mid+1
        else:
            high=mid-1
            index = mid
    return index

def lisUsingBisect(sequence):
    lis = []
    for seq in sequence:
        if len(lis) == 0 or lis[-1] < seq:
            lis.append(seq)
        else:
            index = bisect_left(lis,seq)
            lis[index] = seq
    return len(lis)

print(lis(sequence))
print("bisect 이용",lisUsingBisect(sequence))