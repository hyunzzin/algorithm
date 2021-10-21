# 한방에는 성별, 학년이 같아야 한다.
# 1 <= n <= 1,000
# 1 < k <= 1,000
# 성별 여자 0, 남자 1
# 참가학생수n 한방배정인원k
# n개의 줄 : 학생 성별, 학년
# 남,여 배열 따로 만들기
import sys
n, k = map(int, sys.stdin.readline().split())
std = [[0 for _ in range(7)],[0 for _ in range(7)]]
room = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    std[a][b]+=1
for i in range(7):
    f = std[0][i]
    m = std[1][i]
    if f> 0 and f%k != 0:
        room += (f//k+1)
    elif f>0:
        room+= f//k
    if m > 0 and m%k !=0:
        room += (m//k+1)
    elif m>0:
        room+=m//k

print(room)
