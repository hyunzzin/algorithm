def solution(n, words):
    answer = []
    used = [[] for _ in range(26)]
    turn,start = 0, ''
    for i in range(len(words)):
        turn = i//n+1
        w = words[i]
        if (w in used[ord(w[0])-97] or start != w[0]) and i != 0:
            return [i%n+1,turn]
        used[ord(words[i][0])-97].append(words[i])
        start = w[-1]
    return [0,0]
