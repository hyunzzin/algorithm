'''
영역 구하기
직사각형이 전체를 채우는 경우는 없다

출력
1. 분리되어 나누어지는 영역의 개수
2. 각 영역의 넓이를 오름차순으로 정렬

'''
import sys
from collections import deque

M,N,K = map(int, sys.stdin.readline().split())
paper = [[False for _ in range(N)]for _ in range(M)]
visited = [[False for _ in range(N)]for _ in range(M)]
for _ in range(K):
    y1,x1,y2,x2 = map(int,sys.stdin.readline().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            if not paper[x][y]:
                paper[x][y] = True

def BFS():
    cnt = 0
    que = deque()
    all_area = []
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(M):
        for j in range(N):
            if visited[i][j] or paper[i][j]: continue
            visited[i][j] = True
            que.append((i,j))
            cnt+=1
            area = 1
            while que:
                cur = que.popleft()
                for k in range(4):
                    x = cur[0]+dx[k]
                    y = cur[1]+dy[k]
                    if x<0 or x>=M or y<0 or y>=N:continue
                    if visited[x][y] or paper[x][y]: continue
                    que.append((x,y))
                    visited[x][y]=True
                    area+=1
            all_area.append(area)
                
    return cnt,sorted(all_area)

ans_cnt, ans_area =BFS()
print(ans_cnt)
for a in ans_area:
    print(a,end=' ')

