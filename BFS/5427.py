'''
. : 빈공간
# : 벽
@ : 상근이의 위치
* : 불

불이 없을 수도 있다.
    1. 불의 위치를 que에 넣음
    2. 불이 번지는 시간을 vis_check에 넣는다. 불 초기위치 = 1
    3. 상근이의 위치를 불과 비교한다.
'''

import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

T = int(sys.stdin.readline())
# 상근이 BFS
def SangBFS(sx,sy):
    que = deque()
    que.append((sx,sy))
    vis_check[sx][sy]=1
    while que:
        cur = que.popleft()
        if cur[0] == 0 or cur[0] == h-1 or cur[1] == 0 or cur[1] == w-1:
            return cur
        for k in range(4):
            x = cur[0] + dx[k]
            y = cur[1] + dy[k]
            #print('상근',(x,y))
            if x<0 or x>=h or y<0 or y>=w: continue
            # 방문안한 점이거나 불 속도보다 상근이가 빠르거나
            if (vis_check[x][y]>vis_check[cur[0]][cur[1]]+1 or vis_check[x][y] == 0)and build[x][y] == '.':
                vis_check[x][y] = vis_check[cur[0]][cur[1]]+1
                que.append((x,y))
    return False

def fire():
    # 불의 위치 que에 넣기, 상근이 위치 저장
    sx,sy =0, 0
    for i in range(h):
        for j in range(w):
            if build[i][j] == '*':
                vis_check[i][j] = 1
                que.append((i,j))
            elif build[i][j] == '@':
                sx, sy = i, j
    return sx,sy
def FireBFS():
    # 불 BFS
    while que:
        cur = que.popleft()
        for k in range(4):
            x = cur[0] + dx[k]
            y = cur[1] + dy[k]
            if x<0 or x>=h or y<0 or y>=w: continue
            if not vis_check[x][y] and not build[x][y] == '#': # 불이 지나갈 수 있는 길인 경우
                vis_check[x][y] = vis_check[cur[0]][cur[1]]+1
                que.append((x,y))
    
for _ in range(T):
    build  = []
    que = deque()
    vis_check=[[False for _ in range(1000)]for _ in range(1000)]
    w,h=map(int, sys.stdin.readline().split())
    for _ in range(h):
        build.append(list(sys.stdin.readline().strip('\n')))

    sx,sy = fire()
    FireBFS()            
    cur = SangBFS(sx,sy)
    if cur:
        print(vis_check[cur[0]][cur[1]])
    else:
        print('IMPOSSIBLE')






