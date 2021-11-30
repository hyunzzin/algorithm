'''
감시 4:00
0 : 빈칸
6 : 벽
1-5 : cctv (cctv의 종류)
사각지대의 최소 크기(0의 최소 개수)
O(nm * 4^8) -> 4194304
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
    d %=4 # 4로 나눈 나머지 저장
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











