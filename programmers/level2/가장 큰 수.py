def solution(numbers):
    arr = list(map(str, numbers))
    ans = []
    answer = ''
    # 4자리까지 반복
    for a in arr:
        num = (a*4)[:4]
        len_n = len(a)
        ans.append((num,len_n))
    ans.sort(reverse=True)
    for s,l in ans:
        answer+=s[:l]
    if int(answer) == 0:
        return '0'
    return answer
