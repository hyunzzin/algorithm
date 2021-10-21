'''
import sys
from collections import Counter
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
counter = Counter(sorted(arr))

temp = list(counter.items())
for i in range(len(temp)):
    temp[i] = (temp[i][0],i)
dicttemp = dict(temp)
for j in arr:
    print(dicttemp[j],end=' ')

나보다 작은 수의 개수
counting 이용?
list를 sorted로 정렬
1, 2, 3
중복 개수 찾기
'''
import sys
from collections import Counter
int(sys.stdin.readline())
arr = set(map(int, sys.stdin.readline().split()))
sort_arr = sorted(list(arr))

for i in range(len(sort_arr)):
    sort_arr[i] = (sort_arr[i],i)
sort_arr = dict(sort_arr)

for j in arr:
    print(sort_arr[j],end=' ')

'''
n = int(input())
num_list = list(map(int, input().split()))

num_dict = {}
result_list = []
count = 0

for n in sorted(num_list):
    if n not in num_dict:
        num_dict[n] = count
        count += 1

for n in num_list:
    result_list.append(num_dict[n])

print(str(result_list).replace('[', '').replace(']', '').replace(',', ''))
'''
