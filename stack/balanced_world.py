 #  균형잡힌 세상,4949번
import sys
def parentheses(string):
    stack = []
    for s in string:
        if s=='(' or s=='[':
            if s=='(':
                stack.append(True)
            else:
                stack.append(False)
        elif s==')' or s==']':
            if stack:
                p = stack[-1]
                if p==True and s==')' or p==False and s==']':
                    stack.pop()
                else:
                    return 'no'
            else:
                return 'no'
    if stack:
        return 'no'
    return 'yes'

while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    else:
        print(parentheses(string))
