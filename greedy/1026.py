'''
보물
S를 가장 작게 만들 A의 재배열
B는 재배열하면 안된다.

'''
import sys
N = int(sys.stdin.readline())
A = list(sorted(map(int, sys.stdin.readline().split())))
B = list(sorted(map(int, sys.stdin.readline().split()),reverse=True))
result = 0
for n in range(N):
    result+=A[n]*B[n]
print(result)
