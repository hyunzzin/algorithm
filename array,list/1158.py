'''
문제
사람들이 N만큼 원을 이루면서 앉아있다.
순서대로 K(<=N)번째 사람을 제거한다.
N명이 모두 제거될때까지 계속한다.
사람이 제거되는 순서를 요세푸스 순열(N, K)이라고 한다.

'''
import sys
n, key = map(int, sys.stdin.readline().split()) 
st1 = []
for i in range(1,n+1):
    st1.append(i)

stlen = len(st1)
k = key-1
print('<', end='')
while st1:
    if k >= stlen:
        k %= stlen
    if stlen != 1:
        print(st1.pop(k), end=', ')
    else:
        print(st1.pop(k), end= '')
    k += (key-1)
    stlen-=1
print('>')

