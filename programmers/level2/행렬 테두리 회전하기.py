import sys
def solution(rows, columns, queries):
    arr = []
    cnt = 0
    for _ in range(rows):
        temp = []
        for _ in range(columns):
            cnt+=1
            temp.append(cnt)
        arr.append(temp)
    if len(queries) == 1:
        return [arr[queries[0][0]-1][queries[0][1]-1]]
    ans = []
    for i in range(len(queries)):
        minN = sys.maxsize
        x1,y1,x2,y2 = queries[i]
        x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
        w = y2 - y1
        h = x2 - x1
        memo = arr[x1][y1]
        for k in [1,-1]:
            for _ in range(w):
                memo, arr[x1][y1+k] = arr[x1][y1+k], memo
                minN = min(minN, memo)
                y1 +=k
            for _ in range(h):
                memo, arr[x1+k][y1] = arr[x1+k][y1], memo
                minN = min(minN, memo)
                x1+=k
        ans.append(minN)
    return ans
