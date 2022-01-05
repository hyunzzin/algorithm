'''
로봇 청소기
r : 북쪽으로부터 떨어진 칸의 개수, 행
c : 서쪽으로부터 떨어진 칸의 개수, 열
무조건 왼쪽칸부터 탐색 -> 서/남/동/북
청소할 칸이 없다면 후진
빈칸 : 0 / 벽 : 1

'''
import sys
input = sys.stdin.readline
r,c = map(int, input().split())
x,y,d = map(int, input().split())
Map = []
for _ in range(r):
    Map.append(list(map(int, input().split())))

clean = [[0 for _ in range(c)] for _ in range(r)]
clean[x][y] = 1
direc=0 # 한바퀴 돌았는지 확인
ans = 1
flag = False
while True:  
    # 왼쪽 회전
    if direc < 4:
        d = (d+3)%4
        direc+=1
    elif direc == 4:
        # 후진
        flag = True
        d+=2
        d%=4

    # 회전 방향에 따라 벽인지 칸인지 확인
    if d == 0:
        cx,cy = x-1,y
    elif d == 1:
        cx,cy = x,y+1
    elif d == 2:
        cx,cy = x+1,y
    elif d == 3:
        cx,cy = x,y-1

    # 청소기가 멈추는 조건
    if flag:
        if Map[cx][cy]==1:
            print(ans)
            break
        else:
            # 후진
            flag = False
            x,y=cx,cy
            d+=2
            d %= 4
            direc = 0
    else:
        if clean[cx][cy] or Map[cx][cy]==1: continue
        x,y=cx,cy
        direc = 0
        clean[x][y]=1
        ans+=1
