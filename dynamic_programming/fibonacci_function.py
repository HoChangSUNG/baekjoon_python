#  피보나치 함수
fibo = [[]for _ in range(41)]
fibo[0]=[1,0]  # 0 일때 0,1 호출 개수
fibo[1]=[0,1]  # 1 일때 0,1 호출 개수
def fibonacci(n):
    if fibo[n]:
        return fibo[n]
    else:
        a = fibonacci(n-1)
        b = fibonacci(n-2)
        fibo[n] = [a[0] + b[0], a[1] + b[1]]
        return fibo[n]
testcase = int(input())
for i in range(testcase):
    n = int(input())
    zero, one = fibonacci(n)
    print(zero,one)