# 수 묶기, 1744번
import sys
n = int(sys.stdin.readline().rstrip())
sum = 0
negative=[]# 음수와 0
positive=[]# 양수
for _ in range(n):
    number = int(sys.stdin.readline().rstrip())
    if number<=0:
        negative.append(number)
    else:
        positive.append(number)
negative.sort()
positive.sort(reverse=True)
temp_num=0
for i in range(len(negative)): # 음수와 0 처리
    if i%2==0:
        temp_num=negative[i]
    else:
        sum+=temp_num*negative[i]
if len(negative)%2!=0:
    sum+=temp_num

for i in range(len(positive)):# 양수 처리
    if i%2==0:
        temp_num=positive[i]
    else:
        if temp_num*positive[i]>=temp_num+positive[i]:
            sum+=temp_num*positive[i]
        else: # 정수 1이 포함되어 있을 경우
            sum+=(temp_num+positive[i])
if len(positive)%2!=0:
    sum+=temp_num
print(sum)