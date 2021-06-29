 #  이친수
dp_zero = [0 for i in range(90)]
dp_one = [0 for i in range(90)]
n = int(input())
dp_zero[0] = 0
dp_one[0] = 1
for i in range(1,n):
    dp_zero[i] = dp_zero[i-1]+dp_one[i-1]
    dp_one[i] =  dp_zero[i-1]

print(dp_zero[n-1]+dp_one[n-1])