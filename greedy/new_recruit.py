# 신입사원, 1946번
import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline())
    grade =[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
    grade.sort()
    interview_grade = n+1
    answer = 0
    for i in range(n):
        if grade[i][1]<interview_grade:
            answer += 1
            interview_grade = grade[i][1]
    print(answer)
