'''
회의실 배정
회의 시간이 짧은 순서대로 배정?
끝나는 시간 순으로 정렬
'''
import sys
N = int(sys.stdin.readline())
time = list(sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)], key = lambda x:(x[1],x[0])))
end = 0
result = 0
for n in range(N):
    if time[n][0] >= end: # 시작시간이 같거나 크고
        end=time[n][1]
        print(time[n])
        result +=1
print(result)
