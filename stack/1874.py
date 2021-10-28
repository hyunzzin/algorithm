'''
스택수열
1부터 n까지의 수 k를 스택에 넣었다가 뽑아 늘어놓음
수열이 만들어지지 않으면 NO 반환
'''

import sys
n = int(sys.stdin.readline())
stack = []
answer = []
flag = 1
cur = 1
for _ in range(n):
    k = int(sys.stdin.readline())
    while cur <= k:
        stack.append(cur) # 1부터 k까지 삽입
        answer.append('+')
        cur +=1 
        
    if stack[-1] == k: # 스택의 마지막 숫자가 입력 k와 같으면
        stack.pop()
        answer.append('-')
        
    else:
        print('NO')
        flag=0
        break # sys.exit()을 사용해도 된다.
    
if flag:
    for i in answer:
        print(i)

