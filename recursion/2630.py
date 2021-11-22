'''
색종이 만들기
'''
import sys
n = int(sys.stdin.readline())
paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

ans = [0,0]
'''
함수 정의
    def(x,y,n)
base condition
    색이 다 같으면 탈출
재귀 식
    return def(x+n*i,y+n*i,n)
'''
def check(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def recur(x,y,n):
    if check(x,y,n):
        ans[paper[x][y]]+=1
        return
    n = n//2
    for i in range(2):
        for j in range(2):
            recur(x+n*i,y+n*j,n)
recur(0,0,n)
print(ans[0])
print(ans[1])
