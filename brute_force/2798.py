n, m = map(int, input().split())
arr = list(map(int, input().split()))

def blackJack(n, m, arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1, len(arr)):
                sumB = arr[i]+arr[j]+arr[k]
                if n < sumB and sumB <= m and result < sumB:
                    result = sumB
    return result

print(blackJack(n, m, arr))
