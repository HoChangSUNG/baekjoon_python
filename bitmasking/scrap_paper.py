# 종이조각, 14391번

import sys

def bitmasking():
    result=0
    for num in range(2**(n*m)):

        horizon = 0
        vertical = 0
        #1 ->가로
        #0 ->세로
        for i in range(n):
            curHorizon =0
            for j in range(m):
                idx = m*i+j
                if num&(1<<idx):
                    curHorizon= curHorizon*10+arr[idx]
                else:
                    horizon+=curHorizon
                    curHorizon=0
            horizon+=curHorizon


        for j in range(m):
            curvertical = 0
            for i in range(n):
                idx = m * i + j
                if not (num & (1 << idx)):
                    curvertical=curvertical * 10 + arr[idx]
                else:
                    vertical += curvertical
                    curvertical = 0
            vertical += curvertical

        result = max(result,horizon+vertical)

    return result

n,m = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    arr+=list(map(int,list(sys.stdin.readline().rstrip())))

print(bitmasking())

