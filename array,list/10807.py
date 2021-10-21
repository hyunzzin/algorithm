# 1 <= N <= 100
# -100 <= v <= 100
import sys
input()
arr = list(map(int, sys.stdin.readline().split()))
s = int(input())
print(arr.count(s))
