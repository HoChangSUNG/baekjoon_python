 #  01타일
a,b = 0,1
n = int(input())
for i in range(n):
    a,b = b%15746,(a+b)%15746
print(b)