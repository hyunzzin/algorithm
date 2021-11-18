'''
상범 빌딩
3차원
# : 막혀있는 칸
. : 비어있는 칸
시작점 : S
출구 : E
'''
import sys
from collections import deque
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]

# 층L,행R,열C
def BFS():
    while que:
        cur = que.popleft()
        if build[cur[0]][cur[1]][cur[2]] == 'E':
            return visited[cur[0]][cur[1]][cur[2]]
        for k in range(6):
            z = cur[0] + dz[k]
            x = cur[1] + dx[k]
            y = cur[2] + dy[k]
            if z<0 or x<0 or y<0 or z>=L or x>=R or y>=C:continue
            if visited[z][x][y]==0 and (build[z][x][y]=='.' or build[z][x][y]=='E'):
                visited[z][x][y] = visited[cur[0]][cur[1]][cur[2]]+1
                que.append((z,x,y))
    return False

while True:
    L,R,C = map(int, sys.stdin.readline().split())
    visited = [[[0 for _ in range(C)]for _ in range(R)]for _ in range(L)]
    if L==0 and R==0 and C==0:
        break
    build = []
    que = deque()
    dest = 0
    for l in range(L):
        lst = []
        for r in range(R):
            temp = list(sys.stdin.readline().strip('\n'))
            lst.append(temp)
            if 'S' in temp:
                que.append((l,r,temp.index('S')))
            elif 'E' in temp:
                dest = (l,r,temp.index('E'))
        build.append(lst)
        input()
    

    ans = BFS()

    if ans:
        print('Escaped in',ans,'minute(s).')
    else:
        print('Trapped!')
