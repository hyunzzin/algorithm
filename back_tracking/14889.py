'''
한번의 실패 : set을 사용하지 않고 start를 0과 1만으로 뽑아서 반복문을 돌리려니
오류가 생겼음.
그리고 start와 link를 따로 설정해주지 않아서 해결하지 못함 
import sys
n = int(input())
arr = []
start = []
visit=[]
arr_n = []
for i in range(n):
    visit.append(0)
    arr_n.append(i)
    temp = list(map(int, sys.stdin.readline().split()))
    arr.append(temp)
    
link = []
result = []
minN = sys.maxsize

n_div_2 = n//2
def start_link(x, maxV):
    global n_div_2, result, minN
    
    if x == n_div_2:
        sumV = 0
        # n/2 C 2의 합 구하기
        print('start :',start, visit)
        link = list(set(arr_n)-set(start))
        print('link :', list(set(arr_n)-set(start)))
        # start 안에 있으면 스타트 없으면 링크
        for i in range(n_div_2):
            for j in range(i+1, n_div_2):
                print(i, j)
                sumV += arr[start[i]][start[j]]
                sumV += arr[start[j]][start[i]]
                sumV -= arr[link[i]][link[j]]
                sumV -= arr[link[j]][link[i]]
        if minN > abs(sumV):
            minN = abs(sumV)
    else:
        for i in range(n):
            if visit[i] == 0 and maxV <= i:
                visit[i] = 1
                start.append(i)
                # 자식노드로 이동해서 start에 하나씩 넣는다.
                # 재귀
                start_link(x+1, i)
                # visit를 0으로 바꾼다.
                visit[i] = 0
                start.pop()
    return 0

start_link(0,0)
print(minN)
'''
import sys
n = int(input())
n_div_2 = n//2
arr = []
start = []
visit=[]
arr_n = []
minN = sys.maxsize
for i in range(n):
    visit.append(0)
    arr_n.append(i)
    temp = list(map(int, sys.stdin.readline().split()))
    arr.append(temp)

def start_link(x, maxV):
    global n_div_2, minN
    if x == n_div_2:
        sumV = 0
        link = list(set(arr_n)-set(start))
        for i in range(n_div_2):
            for j in range(i+1, n_div_2):
                sumV += arr[start[i]][start[j]]
                sumV += arr[start[j]][start[i]]
                sumV -= arr[link[i]][link[j]]
                sumV -= arr[link[j]][link[i]]
        if minN > abs(sumV):
            minN = abs(sumV)
    else:
        for i in range(n):
            if visit[i] == 0 and maxV <= i:
                visit[i] = 1
                start.append(i)
                start_link(x+1, i)
                visit[i] = 0
                start.pop()
    return 0

start_link(0,0)
print(minN)
