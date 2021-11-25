'''
N과 M(11)
함수 정의
    def(cnt)
base condition
    if cnt == m:
        print()
        return
재귀 식
    def(cnt+1)
'''
import sys
n,m = map(int, sys.stdin.readline().split())
seq = sorted(list(map(int, sys.stdin.readline().split())))
arr = [False for _ in range(m)]
def bt(cnt):
    if cnt == m:
        print(' '.join(map(str,arr)))
        return
    visit = 0
    for i in range(n):
        if seq[i] != visit:
            visit = seq[i]
            arr[cnt] = seq[i]
            bt(cnt+1)

bt(0)
