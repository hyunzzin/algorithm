'''
import sys
n = int(sys.stdin.readline())
arr = []
sumN = 0
for i in range(n):
    temp = int(sys.stdin.readline())
    sumN += temp
    arr.append(temp)

def statistics(arr):
    # 정렬
    result = sorted(arr)
    '''
    #배열을 돌면서 빈도수 측정
    #기준보다 크면 큰거 저장
    #같으면 또 저장
'''
    mode = [result[0]]
    count = 1
    maxN = 0
    print(result)
    for j in range(len(result)):
        if result[j-1] == result[j]:
            print('첫벙째', result[j], result[j-1])
            count+=1

        if count > maxN:
            print('두벙째',result[j], result[j-1], count, maxN)
            mode = [result[j]]
            maxN = count
            count = 1
        elif count==maxN:
            print(result[j], result[j-1], count, maxN)
            print(count, maxN, '얘네 돌아쪄')
            mode.append(result[j])
            count = 1
    
    # 산술평균
    print(round(sumN/n))
    # 중앙값
    print(result[len(arr)//2])
    # 최빈값
    if len(mode) > 1:
        print(mode[1])
    else:
        print(mode[0])
    # 범위
    print(result[-1]-result[0])
    return 0

statistics(arr)

'''
import sys
from collections import Counter
n = int(sys.stdin.readline())
arr = []
sumN = 0
for i in range(n):
    temp = int(sys.stdin.readline())
    sumN += temp
    arr.append(temp)
def mode(arr):
    counter = Counter(arr)
    if len(counter) == 1: return arr[0]
    counting_arr =counter.most_common(n=2)
    if counting_arr[0][1] == counting_arr[1][1]:
        return counting_arr[1][0]
    return counting_arr[0][0]
        
def statistics(arr):
    result = sorted(arr)
    
    print(round(sumN/n))
    print(result[len(arr)//2])
    print(mode(result))
    print(result[-1]-result[0])

statistics(arr)
