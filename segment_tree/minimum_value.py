import sys
from math import *
sys.setrecursionlimit(10000)

def init(start,end,node):
    if start==end:
        tree[node]=numbers[start]
        return tree[node]

    mid = (start+end)//2
    tree[node]= min(init(start,mid,node*2),init(mid+1,end,node*2+1))
    return tree[node]

def getMin(start,end,node,left,right):
    if start>right or end<left:
        return float('inf')
    if left<=start and end<=right:
        return tree[node]
    mid = (start+end)//2
    return min(getMin(start,mid,node*2,left,right),getMin(mid+1,end,node*2+1,left,right))

n,m = map(int,sys.stdin.readline().rstrip().split())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline().rstrip()))

h = int(ceil(log2(n)))
t_size = 1<<(h+1)
tree = [0]*t_size
init(0,n-1,1)
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print(getMin(0,n-1,1,a-1,b-1))