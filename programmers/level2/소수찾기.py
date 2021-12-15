def num_arr(arr,num, n,a,visited):
    if n ==len(a):
        if int(a) > 1:
            num.add(int(a))
        return
    for j in range(len(arr)):
        if not visited[j]:
            visited[j] = True
            num_arr(arr,num,n,a+arr[j],visited)
            visited[j] = False
def check(k):
    for i in range(2,int(k**(0.5))+1):
        if k%i == 0:
            return False
    return True

def solution(numbers):
    ans = 0
    arr = list(numbers)
    num = set()
    visited = [False for _ in range(len(arr))]
    for i in range(1,len(arr)+1):
        num_arr(arr,num,i,'', visited)
    for k in num:
        if check(k):
            ans+=1
    return ans
