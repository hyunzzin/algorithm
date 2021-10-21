# n개의 서로 다른 양의 정수
# 1 <= a <= 1,000,000
# 1 <= n <= 10,000
# 1 <= x <= 2,000,000
# 쌍의 개수 출력하기
import sys
arr = [False for _ in range(2000001)]
input()
seqs = list(map(int, sys.stdin.readline().split()))
x = int(input())
cnt = 0
for a in seqs:
    if arr[x-a]:
        cnt+=1
    arr[a]=True
print(cnt)

# 메모리 40728이 적고 시간 144ms이 빠름

import sys

n = int(input())
nums = list(map(int,sys.stdin.readline().rstrip().split()))
x = int(input())

count = 0

nums.sort()
# 1 2 3 5 7 9 10 11 12
i = 0
j = len(nums) - 1
while i < j:
    if nums[i] + nums[j] > x:
        j -= 1
    elif nums[i] + nums[j] < x:
        i += 1
    elif nums[i] + nums[j] == x:
        count += 1
        i += 1
        j -= 1

print(count)
