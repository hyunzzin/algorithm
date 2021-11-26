'''
소문난 칠공주
중복 X
함수 정의
    def(cnt)
base condition
    if cnt == 7 and s>= 4:
        ans += 1
재귀 식
    def(cnt)
'''
import sys
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
stu = []
for _ in range(5):
    stu.append(list(sys.stdin.readline().strip('\n')))
visited =  [[False for _ in range(5)]for _ in range(5)]
print(stu)
ans = [0]
def bt(cnt, x, y, S, Y):
    if cnt == 7 and S>=4:
        ans[0]+=1
        return
    if Y>=4:
        return
    for i in range(5):
        for j in range(5):
            for k in range(4):
                curx = x+dx[k]
                cury = y+dy[k]
                if curx<0 or cury<0 or curx>=5 or cury>=5:continue
                visited[curx][cury]= True
                if stu[curx][cury] == 'S': # 현재 학생이 다솜파이면 bt(cnt+1,curx,cury, ans,S+1, Y)
                    bt(cnt+1,curx,cury, S+1, Y)
                elif stu[curx][cury] == 'Y': # 현재 학생이 도연파이면 bt(cnt+1,curx,cury, ans,S, Y+1)
                    bt(cnt+1,curx,cury, S, Y+1)
                visited[curx][cury]= False # visited[curx][cury] 방문 후 나옴
        
            
bt(0,0,0,0,0) 
