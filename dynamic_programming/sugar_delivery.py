n = int(input())  # 설탕 배달
min_p = 987654321
for i in range(n//5+1): # 5의 개수
    k = n
    k -= 5*i
    if k == 0: # 5만으로 kg 다 채우는 경우
        min_p = min(min_p,i)

    elif k%3 == 0: # 3+5의 개수
        min_p = min((min_p,i+k//3))

if min_p== 987654321:
    print(-1)
else:
    print(min_p)