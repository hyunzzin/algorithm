'''
오큰수
숫자를 차례대로 stack에 집어넣는다.
stack의 -1보다 큰 수가 나오면 pop, 그 수를 정답 수열에 넣는다.
stack의 -1보다 작은 수가 나오면 계속 집어넣기
다 돌았을 때 남은 수의 개수만큼 -1을 넣는다.
'''
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = []
stack = []
for i in range(n-1,-1,-1):
    while stack:
        if stack[-1] <= arr[i]:
            stack.pop()
        else:
            ans.append(stack[-1])
            stack.append(arr[i])
            break
    if not stack:
        stack.append(arr[i])
        ans.append(-1)
        
for a in ans[::-1]:
    print(a, end=' ')
