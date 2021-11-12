'''
배추 재배
몇마리의 지렁이가 필요한지
배추가 없는 땅 : 0
배추가 있는 땅 : 1
'''
import sys
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    m,n,k = map(int, sys.stdin.readline().split())
    cab = [[False for _ in range(n)] for _ in range(m)]
    q = deque()
    cnt = 0
    vis_check = [[False for _ in range(50)] for _ in range(50)]
    # 배추 위치 심기
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        cab[x][y] = 1
    for i in range(m):
        for j in range(n):
            if vis_check[i][j] or not cab[i][j]: continue
            q.append((i,j))
            vis_check[i][j] = True
            cnt+=1
            while q:
                cur = q.popleft()
                for p in range(4):
                    cx = cur[0] + dx[p]
                    cy = cur[1] + dy[p]
                    if cx < 0 or cx >= m or cy < 0 or cy >= n: continue
                    if vis_check[cx][cy] or not cab[cx][cy]: continue
                    q.append((cx, cy))
                    vis_check[cx][cy] = True
    print(cnt)                   
