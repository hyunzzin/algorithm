'''
몸무게 : x
키 : y
'''
arr = []
n = int(input())
for i in range(n):
    arr.append(list(map(int, input().split())))
def dungchi(arr):
    for i in range(len(arr)):
        result = 1
        for j in range(len(arr)):
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                result +=1
        print(result, end=' ')
dungchi(arr)
