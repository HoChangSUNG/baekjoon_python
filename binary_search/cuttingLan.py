# 랜선 자르기, 1654번
import sys

def binarySearch(lan,n):
    high=max(lan)
    low = 1
    while low<=high:
        mid = (high+low)//2
        cnt=0
        for number in lan:
            cnt += number//mid

        if cnt<n:
            high=mid-1
        else:
            low = mid+1
    return high

k, n = map(int,sys.stdin.readline().rstrip().split())
lan = []
for _ in range(k):
    lan.append(int(sys.stdin.readline().rstrip()))

print(binarySearch(lan,n))