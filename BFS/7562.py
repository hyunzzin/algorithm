'''
나이트의 이동

'''
import sys
from collections import deque
# 나이트 이동 좌표
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]
T = int(sys.stdin.readline())
for _ in range(T):
    I = int(sys.stdin.readline())
    que = deque()
    # 체스판
    chess = [[0 for _ in range(I)] for _ in range(I)]
    # 나이트가 있는 칸
    curX,curY = map(int,sys.stdin.readline().split())
    arrX,arrY = map(int,sys.stdin.readline().split())
    que.append((curX, curY))
    while que:
        cur = que.popleft()
        if cur[0]== arrX and cur[1] ==arrY:
            print(chess[arrX][arrY])
            break
        for k in range(8):
            x = cur[0]+dx[k]
            y = cur[1]+dy[k]
            if x<0 or x>=I or y<0 or y>=I: continue
            if chess[x][y]:continue
            que.append((x,y))
            chess[x][y] = chess[cur[0]][cur[1]]+1
