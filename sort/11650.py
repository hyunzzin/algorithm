import sys
n = int(input())
result = []
for i in range(n):
    nums = tuple(map(int,sys.stdin.readline().split()))
    result.append(nums)
result.sort()
for x,y in result:
    print(x, y)

'''
import sys
input = sys.stdin.readline 이게 핵심

lst = []

for _ in range(int(input())):
    lst.append(tuple(map(int,input().split())))

lst.sort()

for x,y in lst:
    print(x, y)
'''
