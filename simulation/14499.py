'''
주사위 굴리기
r: 북쪽으로 떨어진 칸의 개수
c: 서쪽으로 떨어진 칸의 개수
지도가 0이면 주사위의 수가 복사됨
0이 아니면 지도가 주사위로 복사, 지도는 0이됨
출력
주사위가 이동했을 때마다 상단에 쓰여 있는 값

지도 바깥으로 이동시 명령 무시
동쪽 이동 - 위-> 동 /아래 -> 서 / 동 -> 아래 / 서 -> 위 / 좌표 y+1
서쪽 이동 - 위-> 서 /아래 -> 동 / 동 -> 위 / 서 -> 아래 / 좌표 y-1
남 <- / 좌표 x+1 rotate(-1)
북 -> / 좌표 x-1 rotate(1)
[서],[위,앞,아래,뒤],[동] 
'''
import sys
from collections import deque
input = sys.stdin.readline
# 지도의 세로N 가로 M, 명령의 개수 K
N,M,x,y,K = map(int, input().split())
Map =[] # 0~9
for _ in range(N):
    Map.append(list(map(int, input().split())))

cmd = list(map(int, input().split()))
dice = [0,deque([0,0,0,0]),0]
# 주사위 이동 -> 수 복사 -> 맨 위 숫자 출력
for i in cmd:
    # 주사위 굴리기
    cx,cy=x,y
    if i == 1: # 동
        cy+=1
        if cy>M-1: continue
        dice[2],dice[1][0] = dice[1][0],dice[2]
        dice[1][2],dice[0] = dice[0],dice[1][2]
        dice[1][0],dice[1][2]=dice[1][2],dice[1][0]
    elif i == 2: # 서
        cy-=1
        if cy<0: continue
        dice[1][0],dice[0] = dice[0],dice[1][0]
        dice[1][2],dice[2] = dice[2],dice[1][2]
        dice[1][0],dice[1][2]=dice[1][2],dice[1][0]
    elif i == 3: # 북
        cx-=1
        if cx<0: continue
        dice[1].rotate(1)
    elif i == 4: # 남
        cx+=1
        if cx>N-1: continue
        dice[1].rotate(-1)
    if cx<0 or cx>N-1 or cy<0 or cy>M-1: continue
    x,y = cx,cy
    if Map[x][y]==0:
        Map[x][y]= dice[1][2]
    else:
        dice[1][2]=Map[x][y]
        Map[x][y]=0
    print(dice[1][0])
