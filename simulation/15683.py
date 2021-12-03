'''
감시 4:00
0 : 빈칸
6 : 벽
1-5 : cctv (cctv의 종류)
사각지대의 최소 크기(0의 최소 개수)
O((4*8*8+64) * 4^8) -> 20971520
cctv 최대 8개
4 2 4 4 1 -> 최대 4가지 

1. 전체 0의 개수 - 감시카메라가 뻗어나간 구역
2. 감시카메라를 회전시키면서 BFS를 돌린다
3. 감시카메라 개수만큼 재귀 (카메라 경우의 수 ^ 카메라 개수)


카메라
- 벽(6)을 만나면 중단
- 다른 카메라(1-5)나 길(0)이면 전진
- 이미 #이면 넘어감

0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
'''
import sys
dx = [1,0,-1,0]
dy = [0,1,0,-1]
n, m = map(int, sys.stdin.readline().split())
place = []
board = [[False for _ in range(10)] for _ in range(10)] # 사각지대 개수 세기
mn = 0 # 빈칸의 개수

# cctv를 찾으면 vector_cctv에 추가
# 사무실 vector 배열 입력
cctv = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    place.append(temp)
    for j in range(m):
        if 0 < temp[j] < 6:
            cctv.append((i,j))
        elif temp[j] == 0:
            mn+=1

def OOB(a,b): # out of bounds 확인 굳이 따로 빼지 않아도 상관없다
    return a<0 or a>=n or b<0 or b>=m

# (x,y)에서 d 방향으로 진행하면서 벽을 만날 때까지 지나치는 모든 빈칸을 7로 바꿈
def upd(x,y,d):
    d %=4 # 방향을 위해서 1을 더할 때 4가 넘는 상황 때문
    while True:
        x+= dx[d]
        y+= dy[d]
        if(OOB(x,y) or board[x][y] == 6): return # 범위를 벗어나거나 벽을 만나면 중단
        if(board[x][y] != 0): continue # 해당 칸이 빈칸이 아닐 경우(=cctv가 있을 경우) 넘어감
        board[x][y] = 7


for tmp in range(4**len(cctv)): # tmp를 4진법으로 뒀을 때 각 자리수를 cctv 방향으로 생각
    for i in range(n):
        for j in range(m):
            board[i][j] = place[i][j]
    brute = tmp # 예를 들면 1~64
    for i in range(len(cctv)):
        d = brute%4 # 나머지를 저장
        brute //= 4 # 몫을 저장
        x,y = cctv[i][0],cctv[i][1]
        if place[x][y] == 1:
            upd(x,y,d)
        elif place[x][y] == 2:
            upd(x,y,d)
            upd(x,y,d+2)
        elif place[x][y] == 3:
            upd(x,y,d)
            upd(x,y, d+1)
        elif place[x][y] == 4:
            upd(x,y,d)
            upd(x,y,d+1)
            upd(x,y,d+2)
        elif place[x][y] == 5:
            upd(x,y,d)
            upd(x,y,d+1)
            upd(x,y,d+2) 
            upd(x,y,d+3) 
    val = 0
    for i in range(n):
        for j in range(m):
            val+= (board[i][j]==0) # 사각지대가 0이니까 true값인 1을 더한다.
    mn = min(mn, val)

print(mn)


'''
300ms
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
ans = 0

def cctv_direction(cctv_type):
    if cctv_type == 1:
        cctv_direction = [[(0,1)],[(0,-1)],[(1,0)],[(-1,0)]]
    if cctv_type == 2:
        cctv_direction = [[(1,0),(-1,0)],[(0,1),(0,-1)]]
    if cctv_type == 3:
        cctv_direction = [[(0,1),(1,0)],[(0,1),(-1,0)],[(0,-1),(1,0)],[(0,-1),(-1,0)]]
    if cctv_type == 4:
        #0,-1 , 1,0 , 0,1 ,- 1,0
        cctv_direction = [[(0,1),(1,0),(-1,0)],[(0,1),(-1,0),(0,-1)],[(0,-1),(1,0),(-1,0)],[(0,-1),(0,1),(1,0)]]
    if cctv_type == 5:
        cctv_direction = [[(0,1),(0,-1),(1,0),(-1,0)]]
    return cctv_direction


def brute(cctvs, cctv_map, counts):
    if not cctvs:
        global ans
        ans = max(ans,counts)
        return counts
    cctv_x, cctv_y, cctv_type = cctvs.pop(0)
    valid_directons = cctv_direction(cctv_type)
    for directions in valid_directons:
        visited = []
        cur_count = 0
        for dx, dy in directions:
            next_x,next_y = cctv_x + dx, cctv_y + dy
            while(0 <= next_x < n and 0 <= next_y < m):
                if cctv_map[next_x][next_y] == 0:
                    cctv_map[next_x][next_y] = -1
                    cur_count += 1
                    visited.append((next_x, next_y)) #변경한 값을 원상 복귀 하기 위해 사용한다.
                elif cctv_map[next_x][next_y] == 6:
                    break
                next_x += dx; next_y += dy
        # for r in cctv_map:
        #     print(r)
        # print("\n\n\n")
        brute(cctvs[:], cctv_map, counts + cur_count)
        for x,y in visited:
            cctv_map[x][y] = 0
    return
    
if __name__ == '__main__':
    cctv_map = [[0 for _ in range(m)] for _ in range(n)]
    cctvs = []
    block_num = 0
    for i in range(n):
        for j,v in enumerate(input().split()):
            v = int(v)
            cctv_map[i][j] = v
            if 0 < v < 6:
                cctvs.append((i,j,v))
            elif v == 6:
                block_num += 1
    cctv_count = len(cctvs)
    brute(cctvs, cctv_map, 0)
    print(m * n - (cctv_count + ans + block_num))
    # print(ans)
'''

'''
140ms
import sys

input = sys.stdin.readline


def move(cx, cy, sdir):
    tmp = set()
    for sd in sdir:
        x, y = cx + px[sd], cy + py[sd]
        while 0 <= x < N and 0 <= y < M:
            if matrix[x][y] == 6:
                break
            elif matrix[x][y] == 0:
                tmp.add((x, y))
            x, y = x + px[sd], y + py[sd]
    return tmp


def check(cnt, cur_set):
    global max_check

    if cnt == cctv:
        max_check = max(max_check, len(cur_set))
        return
    else:
        for p in position[cnt]:
            check(cnt + 1, cur_set | p)


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
px, py = [0, -1, 0, 1], [-1, 0, 1, 0] #서북동남
position, blank, cctv = [], 0, 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            blank += 1
        elif matrix[i][j] == 1:
            position.append([move(i, j, [k]) for k in range(4)])
            cctv += 1
        elif matrix[i][j] == 2:
            position.append([move(i, j, [k, k + 2]) for k in range(2)])
            cctv += 1
        elif matrix[i][j] == 3:
            position.append([move(i, j, [k, (k + 1) % 4]) for k in range(4)])
            cctv += 1
        elif matrix[i][j] == 4:
            position.append([move(i, j, [k, (k + 1) % 4, (k + 2) % 4]) for k in range(4)])
            cctv += 1
        elif matrix[i][j] == 5:
            position.append([move(i, j, [0, 1, 2, 3])])
            cctv += 1

max_check = 0

check(0, set())
print(blank - max_check)
'''






