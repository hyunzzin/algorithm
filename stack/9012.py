import sys
t = int(sys.stdin.readline())
for _ in range(t):
    case = list(sys.stdin.readline().strip('\n'))
    stack = []
    for i in range(len(case)):
        if case[i]=='(':
                stack.append(case[i])
        elif stack:
            if stack[-1]=='(':
                stack.pop()
            else:
                stack.append(case[i])
                break
        else:
            stack.append(case[i])
            break

    if stack:
        print('NO')
    else:
        print('YES')
            
