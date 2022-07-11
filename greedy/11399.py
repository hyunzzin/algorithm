'''
ATM
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값
'''
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = 0
sum_n = 0
for a in range(N):
    sum_n+=arr[a]
    result+= sum_n
print(result)
