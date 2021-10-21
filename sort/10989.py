import sys
n = int(sys.stdin.readline())
aCount=[0]*10001
for i in range(n):
   aCount[int(sys.stdin.readline())]+=1

def counting_sort(aCount):
    for m in range(len(aCount)):
        if aCount[m] == 0: continue
        for o in range(aCount[m]):
            print(m)

counting_sort(aCount)
'''
def counting_sort(arr):
    # 배열 각 숫자 카운팅
    aCount = [0] * (max(arr)+1)
    for j in arr:
        aCount[j] += 1
    # 배열 카운팅 누적합 구하기
    countSum = [0]*(max(arr)+1)
    for k in range(1, len(aCount)):
        countSum[k] = countSum[k-1]+ aCount[k]
    # 배열 정렬
    result = [0] * (n+1)
    for m in range(n-1, -1, -1):
        result[countSum[arr[m]]] = arr[m]
        countSum[arr[m]]-=1
    return result


'''
