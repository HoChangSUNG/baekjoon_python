# 용돈 관리,6236 번
import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
maxOfMoneyPerDay = 100000
money = []
for _ in range(n):
    money.append(int(sys.stdin.readline().rstrip()))

low, high = 1, maxOfMoneyPerDay
while low<=high:
    mid = (low+high)//2
    cost,cnt,index = 0,0,0

    while cnt <= m and index<len(money):
        if cost<money[index]:
            cost = mid
            cnt+=1
        else:
            cost = cost-money[index]
            index+=1
    if cnt>m:
        low = mid+1
    else:
        high = mid-1

print(low)