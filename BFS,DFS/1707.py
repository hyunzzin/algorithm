'''
https://jdselectron.tistory.com/51
'''
import sys
from collections import deque
T = int(sys.stdin.readline())

for _ in range(T):
    flag = True
    ver,tru=map(int,sys.stdin.readline().split())
    v = [False for _ in range(ver+1)]
    visited = [False for _ in range(ver+1)]
    for _ in range(tru):
        a,b = map(int,sys.stdin.readline().split())
        print(a,b)
        if not visited[a] and not visited[b]:
            v[a] = False
            v[b] = True
            visited[a]=True
            visited[b]=True
        elif visited[a] and not visited[b]:
            v[b] = not v[a]
            visited[b] = True
        elif visited[b] and not visited[a]:
            v[a] = not v[b]
            visited[a] = True
        else:
            if v[a] == v[b]:
                flag = False
                break
    if flag:
        print('YES')
    else:
        print('NO')
            
