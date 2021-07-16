# 휴게소 세우기, 1477번
import sys
def binarySearch():
    result = 0
    left = 0
    right = l-1
    while left <= right:
        mid = (left + right)//2
        cnt=0
        for i in range(1,len(stations)):
            if stations[i]-stations[i-1]>mid:
                cnt += (stations[i]-stations[i-1]-1)//mid
        if cnt > m:
            left = mid+1
        else:
            right = mid-1
            result = mid
    return result

n, m, l = map(int,sys.stdin.readline().rstrip().split())
stations = list(map(int,sys.stdin.readline().rstrip().split()))
stations.append(0)
stations.append(l-1)
stations.sort()
print(binarySearch())