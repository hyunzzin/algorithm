def solution(clothes):
    '''
    서로 다른 옷의 조합 수
    '''
    dic = dict()
    for i in clothes:
        if i[1] in dic:
            dic[i[1]].append(i[0])
        else:
            dic[i[1]] = [i[0]]
    ans = 1
    for j in dic:
        ans *= len(dic[j])+1
    return ans-1
