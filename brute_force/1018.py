"""
체스판 다시 칠하기
제자리에 있는 경우 자르기
m부터 m-7까지
n부터 n-7까지
"""
m, n = map(int, input().split())
arr = []
for i in range(m):
    arr.append(input())

# 다시 칠하기 함수
def chess(m, n, arr):
    result = []
    for i in range(m - 7):
        for j in range(n - 7):
            # 한번의 체스판마다 black이 시작인 경우와 white가 시작인 경우의 색칠칸 수
            first = 0
            second = 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if (k + l) % 2 == 1:
                        if arr[k][l] != "B":
                            first += 1
                        else:
                            second += 1
                    elif (k + l) % 2 == 0:
                        if arr[k][l] != "W":
                            first += 1
                        else:
                            second += 1
            result += first, second
    return min(result)


print(chess(m, n, arr))
