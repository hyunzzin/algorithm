# DFS
def check(n,ans,arr,st):
    if ''.join(st)==ans[0]:
        ans[2] = True
        return
    if n==5:
        return
    for i in range(5):
        st.append(arr[i])
        ans[1]+=1
        check(n+1,ans,arr,st)
        st.pop()
        if ans[2]:
            return
        
def solution(word):
    arr = ['A','E','I','O','U']
    st = []
    ans = [word,0,False]
    check(0,ans,arr,st)
    answer = 0
    return ans[1]
