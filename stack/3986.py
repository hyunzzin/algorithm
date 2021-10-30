import sys
n = int(sys.stdin.readline())
result = 0 # 좋은 단어 개수
for _ in range(n):
    S = sys.stdin.readline().strip('\n')
    stack = [] # 좋은 단어 판별 스택
    for s in S:
        if not stack:
            stack.append(s)
        elif s == 'A':
            if stack[-1] == 'A':
                stack.pop()
            else:
                stack.append(s)
        elif s == 'B':
            if stack[-1] == 'B':
                stack.pop()
            else:
                stack.append(s)
    if not stack:
        result +=1
print(result)
