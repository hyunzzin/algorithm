'''
적록색약
빨간색(R) = 초록(G)
색마다 구역의 수를 찾으면 된다.
'''
import sys
from collections import deque

vis_check = [[False for _ in range(5)] for _ in range(5)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
n = int(sys.stdin.readline())
pic = []
for _ in range(n):
    pic.append(list(sys.stdin.readline().strip('\n')))
'''
1. area 구역을 저장한다.
2. que에 값이 같은 문자만 넣는다.
3. 더이상 같은 문자가 없으면 빠져나와 새 문자를 찾는다.
'''
cnt = 0
que = deque()
for i in range(n):
    for j in range(n):
        if vis_check[i][j]: continue
        area = pic[i][j]
        que.append((i,j))
        vis_check[i][j] = True
        cnt+=1
        if pic[i][j] == 'G':
            pic[i][j] = 'R'
        
        while que:
            cur = que.popleft()
            for k in range(4):
                x = cur[0] + dx[k]
                y = cur[1] + dy[k]
                if x < 0 or x >= n or y < 0 or y >= n: continue
                if vis_check[x][y] or pic[x][y] != area: continue
                que.append((x,y))
                vis_check[x][y] = True
                if pic[x][y] == 'G':
                    pic[x][y] = 'R'
print(cnt)
'''
녹색을 적색으로 바꿔서 한번 더 BFS를 돌린다.
'''
cnt = 0
que = deque()
for i in range(n):
    for j in range(n):
        if not pic[i][j]: continue
        area = pic[i][j]
        que.append((i,j))
        cnt+=1
        while que:
            cur = que.popleft()
            for k in range(4):
                x = cur[0] + dx[k]
                y = cur[1] + dy[k]
                if x < 0 or x >= n or y < 0 or y >= n: continue
                if pic[x][y] != area: continue
                que.append((x,y))
                pic[x][y] = False
print(cnt)
















            
