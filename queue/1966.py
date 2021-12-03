'''
프린터 큐
'''
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    ans = 0
    target = q[m]
    imp = sorted(list(q))
    i = imp.pop()
    while True:
        if i == target and m == 0:
            ans+=1
            q.popleft()
            print(ans)
            break
        elif i == q[0]:
            i = imp.pop()
            q.popleft()
            m-=1
            ans+=1
        else:
            q.append(q.popleft())
            if m == 0:
                m = len(q)-1
            else:
                m-=1
        
