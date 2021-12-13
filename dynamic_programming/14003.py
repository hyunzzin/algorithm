import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
lis = []
idx = []
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
            idx.append(index)
            continue
    lis.append(arr[i])
    idx.append(len(lis)-1)

print(len(lis))
len_j = len(idx)-1
ans = [0 for _ in range(len(lis))]
for i in range(len(lis)-1,-1,-1):
    for j in range(len_j,-1,-1):
        if idx[j] == i:
            ans[i] = arr[j]
            len_j = j-1
            break
for k in ans:
    print(k, end=' ')
