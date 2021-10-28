import sys
n = int(sys.stdin.readline())
height = list(map(int, sys.stdin.readline().split()))
stack = []
result = [] # 수신한 탑들의 번호
for i in range(n):
    while stack: # 스택이 비어있지 않으면
        if stack[-1][1] > height[i]: # 수신가능
            result.append(stack[-1][0])
            break
        else: # 수신 불가능
            stack.pop()
            
    if stack == []: # 스택이 비어있으면
        result.append(0)
        
    stack.append([i+1, height[i]])

for r in result:
    print(r, end=' ')
