 #  괄호의 값,2504번
import sys
def value_of_parentheses(string):
    stack = []
    for s in string:
        if s == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(2)
                else:
                    temp = 0 # 숫자들 더해줌.
                    while stack:
                        top = stack.pop()
                        if top == '(':
                            stack.append(2 * temp)  # 곱인 경우
                            break
                        elif top == '[' or len(stack) == 0:  # stack =['[']인 경우, stack=[2, 2, 2]인 경우
                            return 0
                        else:
                            temp += top  # 합인 경우
            else:
                return 0

        elif s == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                    stack.append(3)
                else:
                    temp = 0  # 숫자들 더해줌.
                    while stack:
                        top = stack.pop()
                        if top == '[':
                            stack.append(3 * temp)  # 곱인 경우
                            break
                        elif top == '(' or len(stack) == 0:  # stack =['[']인 경우, stack=[2, 2, 2]인 경우
                            return 0
                        else:
                            temp += top  # 합인 경우
            else:
                return 0
        else:  # s가 '(' or '['인 경우
            stack.append(s)
    answer = 0
    for s in stack:# 올바른 괄호가 아닌 경우->마지막이 열린 괄호('(','[')로 끝난 경우를 확인
        if s == '(' or s == '[':
            return 0
        answer += s
    return answer
n = sys.stdin.readline().rstrip()
print(value_of_parentheses(n))