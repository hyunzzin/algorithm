import sys
count = int(input())
arr= []
for i in range(count):
    arr.append(tuple(map(str, sys.stdin.readline().split())))

arr = sorted(arr, key=lambda x: int(x[0]))
print(arr)
for x, y in arr:
    print(x, y)

'''
import sys


arr = [[] for _ in range(201)]

n = int(sys.stdin.readline())

for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age)
    arr[age].append(name)
for i in range(len(arr)):
    if len(arr[i]) > 0:
        for k in arr[i]:
            print(i, k)

시간, 메모리 측면에서 좋
'''
