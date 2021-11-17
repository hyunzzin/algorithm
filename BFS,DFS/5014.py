'''
스타트링크
F: 총 층수
S: 강호 위치
G: 스타트링크
U: 위로 U층
D: 아래로 D층

도달할 수 없는 경우
1. s>g이고 d가 0인 경우
2. s<g이고 u가 0인 경우
3. u==d이고 수가 그 사이에 있는 경우

70 1 2 2 0
'''
import sys
from collections import deque
f,s,g,u,d = map(int, sys.stdin.readline().split())
build = [False for _ in range(f+1)]
build[s] = 1
def BFS():
    que = deque([s])
    while que:
        if (s>g and d==0)or(s<g and u==0):
            break
        cur=que.popleft()
        for m in [cur+u, cur-d]:
            move = m
            if m<=0 or m>f or build[m]:continue
            build[m]= build[cur]+1
            que.append(m)
    if build[g]:
        return build[g]-1
    else:
        return 'use the stairs'

ans=BFS()
print(ans)

