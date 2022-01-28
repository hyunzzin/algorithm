'''
카드
가장 많이 가지고 있는 정수
sort -> 같은 숫자가 몇개 있는지 구하기
dict에 저장해서 있으면 +1 없으면 x
0 0 1 1 1
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
ans = arr[0]
ans_cnt = 0
cnt = 1
cur = arr[0]
for a in range(1,len(arr)):
    if cur == arr[a]:
        cnt+=1
    else:
        if cnt > ans_cnt:

            ans = cur
            ans_cnt=cnt
        cur = arr[a]
        cnt = 1
if cnt > ans_cnt:

    ans = cur
print(ans)
