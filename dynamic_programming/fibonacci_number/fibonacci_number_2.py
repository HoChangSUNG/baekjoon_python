 #   피보나치 수 2
a = 0
b = 1
n = int(input())
for i in range(n):
    a,b = b,a+b
print(a)