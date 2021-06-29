 # 2 * n 타일링
a,b = 0,1
n = int(input())
for i in range(n):
    a,b = b%10007,(a+b)%10007
print(b)