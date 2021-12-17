'''
D : n을 두배로 바꿈, 9999보다 크면 10000으로 나눈 나머지를 취한다.
S : n에서 1을 뺀 결과 n-1을 레지스터에 저장한다. n이 0이면 9999가 대신 저장
L : n의 각 자리수를 왼쪽으로 회전시켜 저장
R : n의 각 자리수를 오른쪽으로 회전시켜 저
'''
import sys
from collections import deque
input= sys.stdin.readline
def D(n):
    n *=2
    if n > 9999:
        n %=10000
    return n

def S(n):
    if n==0:
        return 9999
    n-=1
    return n

def L(n):
    if not n//1000:
        return n*10
    len_n = len(str(n))-1
    ten = 10**len_n
    add = n//ten
    re = (n%ten) * 10
    return re+add

def R(n):
    if not n//1000:
        return (n%10)*1000 + n//10
    len_n = len(str(n))-1
    ten = 10**(len_n)
    add = (n%10)*ten
    re = n//10
    return re+add
    
ans = []
t = int(input())
for _ in range(t):
    arr = [False for _ in range(10000)]
    a,b = map(int, input().split())
    if a==b:
        print('')
        continue
    n = a
    q = deque()
    dslr_s=['D','S','L','R']
    dslr = [D(n),S(n),L(n),R(n)]
    for i in range(4):
        arr[dslr[i]]= True
        q.append((dslr[i],dslr_s[i]))
    while q:
        cur = q.popleft()
        if cur[0] == b:
            print(cur[1])
            break
        dslr = [D(cur[0]),S(cur[0]),L(cur[0]),R(cur[0])]
        for i in range(4):
            if not arr[dslr[i]]:
                arr[dslr[i]]= True
                q.append((dslr[i],cur[1]+dslr_s[i]))








