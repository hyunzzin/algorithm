'''
가장 긴 증가하는 부분수열
9
10 20 20 5 8 30 10 20 50
'''
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
lis = []
# 이분 탐색
def binary(left,right, target):
    while left < right:
        mid = (left+right)//2
        if lis[mid] < target:
            left = mid+1
        else:
            right = mid
        
    return right

for i in range(len(arr)):
    if lis:
        if lis[-1] >= arr[i]:
            index = binary(0,len(lis)-1, arr[i])
            lis[index] = arr[i]
            continue
    lis.append(arr[i])
print(len(lis))

