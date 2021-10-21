n, m = map(int, input().split())
arr = [0]

def permutation(x):
    if x == m+1:
        print(' '.join(map(str, arr[1:m+1])))
        return
    
    for i in range(1, n+1):
        if max(arr) <= i:
            arr.append(i)
            permutation(x+1)
            arr.pop()

permutation(1)


'''
n,m=map(int,input().split())
result=[]

def dfs(s):
    if len(result) == m:
        print(' '.join(map(str,result)))
        return

    for i in range(s,n+1):
        if i == 0:
            continue
        result.append(i)
        dfs(s)
        result.pop()
        s +=1
dfs(1)
'''
