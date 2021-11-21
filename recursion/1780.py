'''
종이의 개수
1. 종이가 같은 수로 되어 있다면 그대로 사용
2. 같은 수가 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르는 것을 반복한다.
출력
-1 종이 개수
0 종이 개수
1 종이 개수
함수의 정의
    func(x,y,n)
base condition
    ans[paper[x][y]]+=1
    n==1이면 return ans
재귀식
    return func(i*n,J*n,n)
'''
import sys
n = int(sys.stdin.readline())
paper = []
for _ in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))

ans =[0,0,0]

# 같은 숫자인지 확인
def check(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

# 재귀식
def recur(x,y,n):
    # base condition
    if check(x,y,n):
        ans[paper[x][y]]+=1
        return
    n = n//3
    # 쪼개기
    for i in range(3):
        for j in range(3):
            recur(x+i*n,y+j*n,n)
    return 

recur(0,0,n)
print(ans[-1])
print(ans[0])
print(ans[1])
