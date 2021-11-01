'''
경우 나눠서 생각하기
1. 올바른 괄호열인지 먼저 검사

2. (와 [가 들어오면 무조건 스택에 넣는다.
3. ), ]인 경우
    반복해서 stack의 요소를 순회한다.
    stack의 맨 뒤 요소가 (, [이면 stack의 -1에 2, 3을 넣는다.
    stack의 맨 뒤 요소가 (, [이 아니면
        (이면 숫자를 저장해놓은 변수(temp)에 *2, 3을 한다.
        숫자이면 변수(temp)에 저장하고 스택에서 뽑는다.
        
    stack의 합을 반환함
    ((())(())) - 16
    
'''
import sys
S = list(sys.stdin.readline().strip('\n'))     

# 올바른 괄호열인지 검사하는 함수
def is_check(S):
    stack = []
    flag = True
    for s in S:
        if s == '(' or s == '[':
            stack.append(s)
        elif not stack and (s == ')' or s == ']'): # 예외처리
            return False
        elif s == ')':
            if stack[-1] == '(':
                stack.pop()
        elif s == ']':
            if stack[-1] == '[':
                stack.pop()
    if not stack: # 스택이 비어있으면 
        return True
    else:
        return False


    
# 괄호열을 계산하는 함수
def calc(S):
    stack = [] # )] 두가지 경우
    
    for s in S:
        if s == '(' or s == '[':
            stack.append(s)
        else: # )나 ]인 경우
            if s == ')':
                if stack[-1] == '(':
                    stack[-1] = 2
                else: # 다 숫자만 있는 경우
                    temp = 0 # 숫자
                    for st in range(len(stack)-1,-1,-1):
                        if stack[st] == '(': # (2)이런 상황
                            stack[-1]= temp *2
                            break  # 닫는 괄호를 한번 더 만나야하기 때문
                        else: # [ 이라서 숫자를 뽑아서 저장해야 하는 경우
                            temp += stack.pop() # 계속 숫자만 있을 수 있기 때문에 +=를 한다.

            else: # s가 ]인 경우
                if s == ']':
                    if stack[-1] == '[':
                        stack[-1] = 3
                    else:
                        temp = 0
                        for st in range(len(stack)-1,-1,-1):
                            if stack[st] == '[': 
                                stack[-1]= temp *3
                                break
                            else: 
                                temp += stack.pop()
    return sum(stack)



if is_check(S): # 올바른 괄호열이면
    print(calc(S))
else: # 올바른 괄호열이 아니라면
    print(0)


# 같은 부분을 함수로 바꾸기
# 코드는 훨씬 짧아졌다. 메모리나 시간은 똑같다...

import sys
S = list(sys.stdin.readline().strip('\n'))     

# 올바른 괄호열인지 검사하는 함수
def is_check(S):
    stack = []
    for s in S:
        if s == '(' or s == '[':
            stack.append(s)
        elif not stack and (s == ')' or s == ']'):
            return False
        elif s == ')':
            if stack[-1] == '(':
                stack.pop()
        elif s == ']':
            if stack[-1] == '[':
                stack.pop()
    return not bool(stack)

def cal_rpt(stack, n, s):
    if stack[-1] == s:
        stack[-1] = n
    else: 
        temp = 0 
        for st in range(len(stack)-1,-1,-1):
            if stack[st] == s: 
                stack[-1]= temp * n
                break  
            else: 
                temp += stack.pop()
    return stack

def calc(S):
    stack = [] 
    for s in S:
        if s == '(' or s == '[':
            stack.append(s)
        else: 
            if s == ')':
                stack = cal_rpt(stack, 2, '(')
            else: 
                if s == ']':
                    stack = cal_rpt(stack, 3, '[')  
    return sum(stack)

if is_check(S):
    print(calc(S))
else:
    print(0)
















    






        
