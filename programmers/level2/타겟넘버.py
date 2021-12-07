cnt = 0
sumN = 0
def solution(numbers, target, n=0):
    global cnt, sumN
    if n == len(numbers):
        if sumN == target:
            cnt+=1
        return
        
    for j in [1,-1]:
        sumN += (numbers[n]*j)
        solution(numbers, target, n+1)
        sumN -= (numbers[n]*j)
    if n == 0:
        return cnt
