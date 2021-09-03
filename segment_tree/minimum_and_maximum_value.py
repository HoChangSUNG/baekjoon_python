# 최솟값과 최댓값 2357번
import sys
from math import *
sys.setrecursionlimit(10000)

def init(start,end,node):
    if start==end:
        tree[node][0],tree[node][1]=numbers[start],numbers[start]
        return tree[node]

    mid = (start+end)//2
    left_min,left_max = init(start,mid,node*2)
    right_min,right_max = init(mid+1,end,node*2+1)

    tree[node][0]=min(left_min,right_min)
    tree[node][1]=max(left_max,right_max)
    return tree[node]

def getMin(start,end,node,left,right):
    if start>right or end<left:
        return 1000000001
    if left<=start and end<=right:
        return tree[node][0]
    mid = (start+end)//2
    return min(getMin(start,mid,node*2,left,right),getMin(mid+1,end,node*2+1,left,right))

def getMax(start,end,node,left,right):
    if start>right or end<left:
        return 0
    if left<=start and end<=right:
        return tree[node][1]
    mid = (start+end)//2
    return max(getMax(start,mid,node*2,left,right),getMax(mid+1,end,node*2+1,left,right))

n,m = map(int,sys.stdin.readline().rstrip().split())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline().rstrip()))

h = int(ceil(log2(n)))
t_size = 1<<(h+1)
tree = [[0,0]for _ in range(t_size)] # [[최솟값,최대값] ... ]
init(0,n-1,1)
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print(getMin(0,n-1,1,a-1,b-1),getMax(0,n-1,1,a-1,b-1))