'''
N과 M(3)
함수 정의
    def(cnt)
base condition
    if cnt == m:
        print()
        return
재귀식
    def(cnt+1)
'''
import sys
n,m = map(int, sys.stdin.readline().split())
arr = [False for _ in range(m)]

def bt(cnt):
    if cnt == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1,n+1):
        arr[cnt] = i
        bt(cnt+1)
bt(0)










        
