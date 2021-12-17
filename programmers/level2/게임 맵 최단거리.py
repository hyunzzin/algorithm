from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    '''
    BFS
    0 벽이 있는 자리
    1 벽이 없는 자리
    '''
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    go = [[0 for _ in range(m)]for _ in range(n)]
    go[0][0]=1
    q = deque([(0,0)])
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            x=cx+dx[i]
            y=cy+dy[i]
            if x>=n or x<0 or y>=m or y<0: continue
            if maps[x][y] and not go[x][y]:
                go[x][y] = go[cx][cy]+1
                q.append((x,y))
    if go[n-1][m-1]==0:
        return -1
    else:
        return go[-1][-1]
