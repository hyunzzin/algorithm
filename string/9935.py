'''
문자열 폭발
파이썬 배열에서 원소가 같으면 같다는 성질 사용
'''
import sys
arr = list(sys.stdin.readline().strip('\n'))
bomb = list(sys.stdin.readline().strip('\n'))
len_b = len(bomb)
ans = []
for i in range(len(arr)):
    ans.append(arr[i])
    if arr[i]==bomb[-1] and ans[-len_b:] == bomb:
        ans[-len_b:] = []

if ans:
    print(''.join(ans))
else:
    print('FRULA')
