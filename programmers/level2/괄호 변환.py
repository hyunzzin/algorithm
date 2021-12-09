"""
올바른 괄호 문자열인지 검사
    
균형잡힌 괄호 문자열인 경우
1. 균형잡힌 문자열 분리 u,v / 단, u는 균형 유지 - 균형 체크, 올바른지 체크
2. 문자열 u가 올바른 괄호 문자열인지 판단
    if 올바른 경우 -> 다시 분리 solution
    else 올바르지 않는 경우
        - 빈 문자열에 첫 번째 문자로 '('붙임
        - v를 가지고 다시 solution 실행
        - ')' 붙임
        - u의 첫번째와 마지막을 제거, 나머지 문자열 뒤집음, 뒤에 붙임
        - 문자열 반환    
"""
from collections import deque

# 균형잡힌 괄호 u와 v로 나누기
def div(p):
    p = list(p)
    st = 0
    for i in range(len(p)):
        if p[i] == "(":
            st += 1
        else:
            st -= 1
        if i != 0 and st == 0:
            return deque(p[: i + 1]), deque(p[i + 1 :])
    return deque(p), ""


# 올바른 괄호인지 판별
def check(u):
    st = []
    for i in u:
        if i == "(":
            st.append("(")
        else:
            if not st:
                return False
            st.pop()
    if not st:
        return True
    return False


def solution(p):
    if not len(p):
        return ""
    u, v = div(p)
    correct = check(u)
    if correct:
        ans = solution(v)
        return "".join(u) + "".join(ans)
    # u가 올바른 괄호 아닌경우
    s = ["("]
    s.extend(solution(v))
    s.append(")")
    u.popleft()
    u.pop()
    for i in u:
        if i == "(":
            s.append(")")
        else:
            s.append("(")
    return "".join(s)
