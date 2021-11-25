'''
N과 M(8)
함수 정의
    def(cnt, k)
base condition
    if cnt == m:
        print()
        return
재귀 식
    def(cnt+1, i)

'''
import sys
n,m = map(int, sys.stdin.readline().split())
seq = sorted(list(map(int, sys.stdin.readline().split())))
arr = [False for _ in range(m)]

def bt(cnt, k):
    if cnt == m:
        print(' '.join(map(str,arr)))
        return
    for i in range(k,n):
        arr[cnt] = seq[i]
        bt(cnt+1,i)
bt(0,0)
