import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]

# merge sort를 구현하는 것보다 sort 메소드가 더 빠름
arr.sort()
for a in arr:
    print(a)
