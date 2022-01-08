'''
시리얼 번호
길이가 짧은 것이 먼저 온다.
길이가 같으면 자리수의 합, 작은 합이 먼저 옴
1,2번으로 안되면 사전순으로 비교
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    num = input().strip('\n')
    sumN = 0
    for n in num:
        if n.isdigit():
            sumN += int(n)
    arr.append((len(num),sumN,num))
arr.sort()
for a in arr:
    print(a[2])
    
