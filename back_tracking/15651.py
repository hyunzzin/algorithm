# 1부터 N까지 중복 없이 M개를 고른 수열
# permutation, 순열에 관한 문제이다.
n, m = map(int, input().split())
arr = [0]*(m+1)

def permutation(x):
    if x == m+1:
        for i in arr[1:m+1]:
            print(i, end = ' ')
        print()
        '''
        1등 제일빠름 1840ms
        print(' '.join(map(str, arr[1:m+1]))) 

        2등 2948ms
        for i in arr[1:m+1]:
            print(i, end = ' ')
        print()

        3등 3160ms
        for i in range(1, m+1):
            print(arr[i], end = ' ')
        print()
        '''
    else:
        for i in range(1, n+1):
            arr[x] = i
            permutation(x+1)
            arr[x] = 0

permutation(1)
