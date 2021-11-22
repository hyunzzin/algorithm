'''
쿼드트리
'''
import sys
n = int(sys.stdin.readline())
vdo=[]
for _ in range(n):
    vdo.append(list(map(int,sys.stdin.readline().strip('\n'))))
'''
함수 정의
    def(x,y,n)
base condition
    다 같으면 출력
재귀 식
    def(x+i*n,y+j*n,n//2)
'''
def check(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if vdo[x][y] != vdo[i][j]:
                return False
    return True

def recursion(x,y,n):
    
    if check(x,y,n):
        print(vdo[x][y],end='')
        return
    
    n=n//2
    print('(',end='')
    for i in range(2):
        for j in range(2):
            
            recursion(x+i*n,y+j*n,n)
            
    print(')',end='')   
recursion(0,0,n)
